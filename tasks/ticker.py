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


def _process(logger, exchange_class, schema_class, symbol):
    try:
        ticker_data = exchange_class().get_ticker(
            symbol=symbol
        )
    except ValueError as err:
        logger.error(err)
        return
    ticker_data_valid, errors = schema_class().load(ticker_data)
    assert errors == {}, errors
    ticker_model = TickerModel(**ticker_data_valid)
    ticker_model.save()


def _get_24h_price_ticker_data(
        jobs, logger, exchange_class, schema_class, symbol
):
    p = Process(
        target=_process, args=(
            logger, exchange_class, schema_class, symbol
        )
    )
    jobs.append(p)
    p.start()


def _terminate_running_jobs(jobs):
    for j in jobs:
        if j.is_alive():
            j.terminate()
            j.join()


@task(bind=True)
@use_mongodb(connect=False)
def update(self):
    jobs = []
    logger = self.get_logger()
    try:
        for exchange, symbols in s.EXCHANGES_AND_SYMBOLS.items():
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
            for coin, quote in symbols.items():
                _get_24h_price_ticker_data(
                    jobs, logger, exchange_class, schema_class,
                    symbol=[coin, quote]
                )
        for j in jobs:
            j.join(timeout=s.TIMEOUT_CONNECTION_PER_SYMBOL)
    except ValueError as error:
        _terminate_running_jobs(jobs)
        self.update_state(state=states.FAILURE, meta=str(error))
        raise Ignore()
    finally:
        _terminate_running_jobs(jobs)


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
