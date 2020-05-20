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
from billiard.context import Process
from flask_socketio import SocketIO
from xtcryptosignals.tasks.celeryconfig import BROKER_URL
from binance.client import Client
from xtcryptosignals.tasks.ticker import _terminate_running_jobs
from xtcryptosignals.tasks import settings as s


socketio = SocketIO(message_queue=BROKER_URL)


def _get_intervals(k, _order_book, totals):
    n = 10
    _intervals = []
    a, b = (0, -1) if k == "asks" else (-1, 0)
    for x in [_order_book[i : i + n] for i in range(0, len(_order_book), n)]:
        v = x[-1][-2]
        _intervals.append([x[a][0], x[b][0], v, int((v / totals[k]) * 100)])
    return _intervals


def _process(logger, symbol):
    client = Client(s.BINANCE_API_KEY, s.BINANCE_API_SECRET)

    order_book = client.get_order_book(symbol=symbol)

    _order_book = {
        "asks": [],
        "bids": [],
        "asks_cumulative": [],
        "bids_cumulative": [],
    }

    # get totals
    totals = {"asks": 0.0, "bids": 0.0}
    for k in (
        "asks",
        "bids",
    ):
        totals[k] = sum([float(x[1]) for x in order_book[k]])

    for k, o in (
        ("asks", False),
        ("bids", True),
    ):
        accrued = 0.0
        for n1, n2 in sorted(order_book[k], reverse=o):
            _n1 = float(n1)
            _n2 = float(n2)
            _order_book[k].append([_n1, _n2, int((_n2 / totals[k]) * 100)])
            accrued += _n2
            _order_book[k + "_cumulative"].append(
                [_n1, float(accrued), int((accrued / totals[k]) * 100)]
            )

    _order_book["bids"] = [x for x in reversed(_order_book["bids"])]

    for x in (
        "asks",
        "bids",
    ):
        xx = f"{x}_cumulative"
        _order_book[f"intervals_{xx}"] = _get_intervals(
            x, _order_book[xx], totals
        )

    _order_book["bids_cumulative"] = [
        x for x in reversed(_order_book["bids_cumulative"])
    ]

    socketio.emit("order_book", _order_book, namespace=f"/order_book/{symbol}")


@task(bind=True)
def update(self):
    logger = self.get_logger()
    jobs = []

    try:
        for coin_or_token, quote in s.SYMBOLS_PER_EXCHANGE[0][s.BINANCE][
            "pairs"
        ]:
            symbol = coin_or_token + quote

            p = Process(name=symbol, target=_process, args=(logger, symbol,),)

            jobs.append(dict(job=p, timeout=s.ORDER_BOOK))

            p.start()

        for j in jobs:
            j["job"].join(timeout=j["timeout"])

    except Exception as error:
        _terminate_running_jobs(logger, jobs)
        logger.error("order_book error: {}".format(str(error)))
        self.update_state(state=states.FAILURE, meta=str(error))
        raise Ignore()
    finally:
        _terminate_running_jobs(logger, jobs)
