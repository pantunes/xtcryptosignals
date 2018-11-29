__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import sys
import os
from celery.task import task
from celery.exceptions import Ignore
from celery import states
from billiard.context import Process
sys.path.append(os.getcwd())
import settings as s  # noqa
from utils.decorators import use_mongodb  # noqa
from utils.helpers import get_class  # noqa
from models.ticker import Ticker as TickerModel  # noqa


def _process(logger, exchange_class, schema_class, symbol, pairs):
    ticker_kwargs = dict()
    if symbol:
        ticker_kwargs.update(symbol=symbol)
    elif pairs:
        ticker_kwargs.update(pairs=pairs)
    else:
        logger.error(
            'Error in {} Not either a symbol or pair', exchange_class.__name__
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
    if pairs:
        for x in ticker_data_valid:
            ticker_model = TickerModel(**x)
            ticker_model.save()
    else:
        ticker_model = TickerModel(**ticker_data_valid)
        ticker_model.save()


def _get_24h_price_ticker_data(
        jobs, logger, exchange_class, schema_class, symbol=None, pairs=None
):
    symbol_or_pairs = '-'.join(symbol) if symbol else 'PAIRS'
    p = Process(
        name='{} {}'.format(exchange_class.__name__, symbol_or_pairs),
        target=_process,
        args=(
            logger, exchange_class, schema_class, symbol, pairs
        )
    )
    jobs.append(p)
    p.start()


def _terminate_running_jobs(logger, jobs):
    for j in jobs:
        if j.is_alive():
            logger.warning('Timeout in {}'.format(j.name))
            j.terminate()
            j.join()


@task(bind=True)
@use_mongodb(connect=False)
def update(self):
    jobs = []
    logger = self.get_logger()
    try:
        for row in s.EXCHANGES_AND_SYMBOLS:
            exchange = list(row.keys())[0]
            pairs = row[exchange]['pairs']
            try:
                exchange_class = get_class(
                    folder='exchanges', module=exchange
                )
            except ModuleNotFoundError as err:
                logger.error(err)
                continue
            try:
                schema_class = get_class(
                    folder='schemas', module=exchange
                )
            except ModuleNotFoundError as err:
                logger.error(err)
                continue
            single_request = row[exchange].get('single_request')
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
            j.join(timeout=s.TIMEOUT_PER_SYMBOL_REQUEST)
    except ValueError as error:
        _terminate_running_jobs(logger, jobs)
        self.update_state(state=states.FAILURE, meta=str(error))
        raise Ignore()
    finally:
        _terminate_running_jobs(logger, jobs)


if __name__ == "__main__":
    import logging
    logging.basicConfig(
        format='%(asctime)s %(levelname)s %(message)s',
        level=logging.INFO,
    )
    from multiprocessing import Process
    logging.info('starting job...')
    update()
    logging.info('ending job...')
