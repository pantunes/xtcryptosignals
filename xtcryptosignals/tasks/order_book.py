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
from binance.client import Client as BinanceClient

try:
    from idex.client import Client as IdexClient
except ModuleNotFoundError:
    pass
from xtcryptosignals.tasks.utils import terminate_running_jobs
from xtcryptosignals.tasks import settings as s


ORDER_BOOK_BINANCE_LIMIT = 100
ORDER_BOOK_BINANCE_OFFSET = int(ORDER_BOOK_BINANCE_LIMIT / 10)

ORDER_BOOK_IDEX_LIMIT = 100
ORDER_BOOK_IDEX_OFFSET = int(ORDER_BOOK_IDEX_LIMIT / 10)


socketio = SocketIO(message_queue=BROKER_URL)


def _get_intervals(k, _order_book, totals, offset):
    _intervals = []
    a, b = (0, -1) if k == "asks" else (-1, 0)
    for x in [
        _order_book[i : i + offset] for i in range(0, len(_order_book), offset)
    ]:
        v = x[-1][-2]
        _intervals.append([x[a][0], x[b][0], v, int((v / totals[k]) * 100)])
    return _intervals


def _process_idex(_, symbol):
    client = IdexClient(s.IDEX_API_KEY, s.IDEX_ADDRESS, s.IDEX_PRIVATE_KEY)

    order_book = client.get_order_book(
        market="_".join(reversed(symbol)), count=100
    )

    _order_book = {
        "asks": [],
        "bids": [],
    }

    for x in (
        "asks",
        "bids",
    ):
        for xx in order_book[x]:
            _order_book[x].append([xx["price"], xx["amount"]])

    _process("{}{}".format(*symbol), _order_book, offset=ORDER_BOOK_IDEX_OFFSET)


def _process_binance(_, symbol):
    client = BinanceClient(s.BINANCE_API_KEY, s.BINANCE_API_SECRET)

    _symbol = "{}{}".format(*symbol)
    order_book = client.get_order_book(
        symbol=_symbol, limit=ORDER_BOOK_BINANCE_LIMIT
    )

    _process(_symbol, order_book, offset=ORDER_BOOK_BINANCE_OFFSET)


def _process(symbol, order_book, offset):
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
            x, _order_book[xx], totals, offset=offset
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
        for coin_or_token, struct in s.EXCHANGES_AND_PAIRS_OF_REFERENCE.items():

            if "market_depth" not in struct:
                continue

            md = struct["market_depth"]
            quotes = md["pairs"]
            exchange = md["exchange"]

            _method = globals()[f"_process_{exchange}"]

            for quote in quotes:
                p = Process(
                    name=f"{coin_or_token}-{quote}",
                    target=_method,
                    args=(
                        logger,
                        (
                            coin_or_token,
                            quote,
                        ),
                    ),
                )
                jobs.append(dict(job=p, timeout=s.TIMEOUT_ORDER_BOOK))
                p.start()

        for j in jobs:
            j["job"].join(timeout=j["timeout"])

    except Exception as error:
        logger.error(f"order_book error: {error}")
        self.update_state(state=states.FAILURE, meta=str(error))
        raise Ignore()
    finally:
        terminate_running_jobs(logger, jobs)
