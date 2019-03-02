__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import click
from celery.task import task
from celery.exceptions import Ignore
from celery import states
from billiard.context import Process
from pymongo.errors import ServerSelectionTimeoutError
from flask_socketio import SocketIO
import xtcryptosignals.settings as s
from xtcryptosignals.celeryconfig import BROKER_URL
from xtcryptosignals.storage.service import use_mongodb
from xtcryptosignals.utils.helpers import get_class
from xtcryptosignals.models.ticker import Ticker as TickerModel


def _process(
        logger, socketio, exchange_class, schema_class, symbol, pairs
):
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

    ticker, errors = schema_class(
        strict=True,
        many=symbol is None
    ).load(ticker_data)
    assert errors == {}, errors

    try:
        if pairs:
            for x in ticker:
                ticker_model = TickerModel(**x)
                history_dicts = ticker_model.save()
                if socketio:
                    for h in history_dicts:
                        socketio.emit(
                            'ticker', h, namespace='/{}'.format(h['frequency'])
                        )
        else:
            ticker_model = TickerModel(**ticker)
            history_dicts = ticker_model.save()
            if socketio:
                for h in history_dicts:
                    socketio.emit(
                        'ticker', h, namespace='/{}'.format(h['frequency'])
                    )

    except ServerSelectionTimeoutError as error:
        logger.error(
            '{}: {}'.format(exchange_class.__name__, error)
        )


def _get_24h_price_ticker_data(
        jobs, logger, exchange_class, schema_class,
        symbol=None, pairs=None
):
    socketio = None
    if _ENABLE_SOCKET_IO:
        socketio = SocketIO(message_queue=BROKER_URL)

    symbol_or_pairs = '-'.join(symbol) if symbol else 'PAIRS'

    p = Process(
        name='{} {}'.format(exchange_class.__name__, symbol_or_pairs),
        target=_process,
        args=(
            logger, socketio, exchange_class,
            schema_class, symbol, pairs,
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


_ENABLE_SOCKET_IO = False


@click.command(
    context_settings=dict(help_option_names=['-h', '--help'])
)
@click.option(
    '--testing',
    is_flag=True,
    help="Execute 1 iteration for all configured "
         "coins and/or tokens without Celery. "
         "(Useful for testing purposes)",
)
@click.option(
    '--list-config',
    type=click.Choice(['exchanges', 'currencies']),
    help="List 'exchanges' or 'currencies' (coins or tokens) per exchange "
         "that the tool currently supports."
)
@click.option(
    '--enable-real-time-messaging',
    is_flag=True,
    help="Enable SocketIO real-time crypto-data message broadcasting."
)
@click.option(
    '--version',
    is_flag=True,
    help="Show version."
)
def main(testing, list_config, enable_real_time_messaging, version):
    """
    Use this tool to collect data from configured coins or/and tokens from
    configured crypto-currencies exchanges.
    """
    if list_config:
        if list_config == 'currencies':
            import pprint
            click.echo(pprint.pprint(s.SYMBOLS_PER_EXCHANGE))
        if list_config == 'exchanges':
            click.echo('\n'.join(s.EXCHANGES))
        return

    if testing:
        test()
        return

    if version:
        from xtcryptosignals import __title__, __version__
        click.echo('{} {}'.format(__title__, __version__))
        return

    global _ENABLE_SOCKET_IO
    _ENABLE_SOCKET_IO = enable_real_time_messaging

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
