__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from celery.task import task
from celery.exceptions import Ignore
from celery import states
from billiard.context import Process
from pymongo.errors import ServerSelectionTimeoutError
import xtcryptosignals.settings as s
from xtcryptosignals.utils.decorators import use_mongodb
from xtcryptosignals.utils.helpers import get_class
from xtcryptosignals.models.ticker import Ticker as TickerModel


def _process(logger, exchange_class, schema_class, symbol, pairs):
    ticker_kwargs = dict()
    if symbol:
        ticker_kwargs.update(symbol=symbol)
    elif pairs:
        ticker_kwargs.update(pairs=pairs)
    else:
        logger.error(
            '{}: Not either a symbol or pair'.format(exchange_class.__name__)
        )
    try:
        ticker_data = exchange_class().get_ticker(**ticker_kwargs)
    except ValueError as err:
        logger.error(err)
        return

    ticker_data_valid, errors = schema_class(
        many=symbol is None
    ).load(ticker_data)
    assert errors == {}, errors

    try:
        if pairs:
            for x in ticker_data_valid:
                ticker_model = TickerModel(**x)
                ticker_model.save()
        else:
            ticker_model = TickerModel(**ticker_data_valid)
            ticker_model.save()
    except ServerSelectionTimeoutError as error:
        logger.error(
            '{}: {}'.format(exchange_class.__name__, error)
        )


def _get_24h_price_ticker_data(
        jobs, logger, exchange_class, schema_class,
        symbol=None, pairs=None
):
    symbol_or_pairs = '-'.join(symbol) if symbol else 'PAIRS'
    p = Process(
        name='{} {}'.format(exchange_class.__name__, symbol_or_pairs),
        target=_process,
        args=(
            logger, exchange_class, schema_class, symbol, pairs
        )
    )
    jobs.append(
        dict(
            job=p,
            timeout=s.TIMEOUT_PER_SYMBOL_REQUEST
            if symbol else s.TIMEOUT_PER_SYMBOLS_REQUEST
        )
    )
    p.start()


def _terminate_running_jobs(logger, jobs):
    for j in jobs:
        if j['job'].is_alive():
            logger.warning('Exceeded timeout of {} in {}'.format(
                j['timeout'], j['job'].name)
            )
            j['job'].terminate()
            j['job'].join()


@task(bind=True)
@use_mongodb(connect=False)
def update(self):
    jobs = []
    logger = self.get_logger()
    try:
        for row in s.SYMBOLS_PER_EXCHANGE:
            for exchange, data in row.items():
                pairs = data['pairs']
                if not pairs:
                    logger.info('No pairs for {}'.format(exchange))
                    continue
                try:
                    exchange_class = get_class(
                        folder='xtcryptosignals.exchanges', module=exchange
                    )
                except ModuleNotFoundError as err:
                    logger.error(err)
                    continue
                try:
                    schema_class = get_class(
                        folder='xtcryptosignals.schemas', module=exchange
                    )
                except ModuleNotFoundError as err:
                    logger.error(err)
                    continue
                single_request = data.get('single_request')
                if not single_request:
                    for coin, quote in pairs:
                        _get_24h_price_ticker_data(
                            jobs, logger, exchange_class, schema_class,
                            symbol=[coin, quote]
                        )
                else:
                    _get_24h_price_ticker_data(
                        jobs, logger, exchange_class, schema_class,
                        pairs=pairs
                    )
        for j in jobs:
            j['job'].join(timeout=j['timeout'])
    except ValueError as error:
        _terminate_running_jobs(logger, jobs)
        self.update_state(state=states.FAILURE, meta=str(error))
        raise Ignore()
    finally:
        _terminate_running_jobs(logger, jobs)


def test():
    import logging
    logging.basicConfig(
        format='%(asctime)s %(levelname)s %(message)s',
        level=logging.INFO,
    )
    logging.info('Testing Ticker without Celery')
    logging.info('Starting...')
    update()
    logging.info('Ending...')


def main():
    from celery import current_app
    from celery.bin import worker

    app = current_app._get_current_object()
    app.config_from_object('xtcryptosignals.celeryconfig')

    worker = worker.worker(app=app)
    options = {
        'beat': True,
        'loglevel': 'INFO',
    }
    worker.run(**options)


if __name__ == "__main__":
    main()
