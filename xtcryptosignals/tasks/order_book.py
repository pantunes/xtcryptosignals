__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from celery.task import task
from celery.exceptions import Ignore
from celery import states
from flask_socketio import SocketIO
from xtcryptosignals.tasks.celeryconfig import BROKER_URL
from binance.client import Client
from xtcryptosignals.tasks import settings as s


socketio = SocketIO(message_queue=BROKER_URL)


@task(bind=True)
def update(self, pairs):
    logger = self.get_logger()

    try:
        client = Client(s.BINANCE_API_KEY, s.BINANCE_API_SECRET)

        for coin_or_token, pair in pairs:
            order_book = client.get_order_book(symbol=pair)

            _order_book = {}
            for k, o in (('bids', True), ('asks', False),):
                _order_book[k] = []
                accrued = 0.0
                for n1, n2 in sorted(order_book[k], reverse=o):
                    accrued += float(n2)
                    _order_book[k].append([float(n1), float(accrued)])

            socketio.emit(
                "order_book",
                _order_book,
                namespace=f"/order_book/{coin_or_token}"
            )
    except ValueError as error:
        logger.error("order_book error: {}".format(str(error)))
        self.update_state(state=states.FAILURE, meta=str(error))
        raise Ignore()
