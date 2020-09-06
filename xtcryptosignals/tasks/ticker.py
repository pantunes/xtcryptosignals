__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import logging
from celery.task import task
from celery.exceptions import Ignore
from celery import states
from billiard.context import Process
from pymongo.errors import ServerSelectionTimeoutError
from flask_socketio import SocketIO
from xtcryptosignals.tasks.celeryconfig import BROKER_URL
from xtcryptosignals.common.utils import use_mongodb
from xtcryptosignals.tasks.utils import (
    get_class,
    terminate_running_jobs,
)
from xtcryptosignals.tasks.models.ticker import Ticker
from xtcryptosignals.tasks import settings as s


@use_mongodb(db=s.MONGODB_NAME, host=s.MONGODB_HOST, port=s.MONGODB_PORT)
def _process(logger, socketio, exchange_class, schema_class, symbol, pairs):
    ticker_kwargs = {}
    if symbol:
        ticker_kwargs.update(symbol=symbol)
    elif pairs:
        ticker_kwargs.update(pairs=pairs)
    else:
        logger.error(
            "{}: Not either a symbol or pair".format(exchange_class.__name__)
        )
    try:
        ticker_data = exchange_class().get_ticker(**ticker_kwargs)
    except ValueError as err:
        logger.error(err)
        return

    ticker, errors = schema_class(strict=True, many=symbol is None).load(
        ticker_data
    )
    assert errors == {}, errors

    try:
        if not pairs:
            ticker = (ticker,)
        for x in ticker:
            ticker_model = Ticker(**x)
            ticker_model.save(temporary=not s.CREATE_MODEL_TICKER)
            if socketio:
                for h in ticker_model.get_history():
                    socketio.emit(
                        "ticker", h, namespace="/{}".format(h["frequency"])
                    )
    except ServerSelectionTimeoutError as error:
        logger.error("{}: {}".format(exchange_class.__name__, error))


def _get_24h_price_ticker_data(
    jobs,
    logger,
    exchange_class,
    schema_class,
    symbol=None,
    pairs=None,
    *_,
    **kwargs
):
    socketio = None

    if not kwargs["disable_ticker_messaging"]:
        socketio = SocketIO(message_queue=BROKER_URL)

    symbol_or_pairs = "-".join(symbol) if symbol else "PAIRS"

    p = Process(
        name="{} {}".format(exchange_class.__name__, symbol_or_pairs),
        target=_process,
        args=(logger, socketio, exchange_class, schema_class, symbol, pairs,),
    )
    jobs.append(
        dict(
            job=p,
            timeout=s.TIMEOUT_PER_SYMBOL_REQUEST
            if symbol
            else s.TIMEOUT_PER_SYMBOLS_REQUEST,
        )
    )
    p.start()


@task(bind=True)
def update(self, *_, **kwargs):
    if not kwargs["disable_ticker_messaging"]:
        log_level = (
            logging.INFO if not kwargs["log_ticker_minimal"] else logging.ERROR
        )
        logging.getLogger("engineio").setLevel(log_level)
        logging.getLogger("socketio").setLevel(log_level)

    logger = self.get_logger()
    jobs = []

    try:
        for row in s.SYMBOLS_PER_EXCHANGE:
            for exchange, data in row.items():
                pairs = data["pairs"]
                if not pairs:
                    logger.info("No pairs for {}".format(exchange))
                    continue
                try:
                    exchange_class = get_class(
                        folder="xtcryptosignals.tasks.exchanges",
                        module=exchange,
                    )
                except ModuleNotFoundError as err:
                    logger.error(err)
                    continue
                try:
                    schema_class = get_class(
                        folder="xtcryptosignals.tasks.schemas", module=exchange
                    )
                except ModuleNotFoundError as err:
                    logger.error(err)
                    continue
                single_request = data.get("single_request")
                if not single_request:
                    for coin, quote in pairs:
                        _get_24h_price_ticker_data(
                            jobs,
                            logger,
                            exchange_class,
                            schema_class,
                            symbol=[coin, quote],
                            **kwargs
                        )
                else:
                    _get_24h_price_ticker_data(
                        jobs,
                        logger,
                        exchange_class,
                        schema_class,
                        pairs=pairs,
                        **kwargs
                    )

        for j in jobs:
            j["job"].join(timeout=j["timeout"])

    except Exception as error:
        logger.error("ticker error: {}".format(str(error)))
        self.update_state(state=states.FAILURE, meta=str(error))
        raise Ignore()
    finally:
        terminate_running_jobs(logger, jobs)


def test(*_, **kwargs):
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO,
    )
    logging.info("Process 1 Tick")
    logging.info("Starting...")
    update(**kwargs)
    logging.info("Ending...")
