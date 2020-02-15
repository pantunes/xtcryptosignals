__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"

import pytz
from datetime import datetime
from xtcryptosignals.tasks.models.history import History
from xtcryptosignals.tasks.models.cfgi import CFGI
from xtcryptosignals.tasks import settings as s


NUM_OCCURRENCES = 30  # CFGI_MIN=1d in client


def get_chart_fear_and_greed_index_and_btc(frequency):
    model_history = type("History{}".format(frequency), (History,), {})
    rows = model_history.objects(symbol="BTCUSDT", source="binance",)[
        :NUM_OCCURRENCES
    ]

    btc_prices = {
        x.created_on.strftime("%Y-%m-%d"): int(x.price_usdt) for x in rows
    }

    days = [x.created_on.strftime("%Y-%m-%d") for x in rows]
    days.reverse()

    cfgi_values = {
        x.added_on.strftime("%Y-%m-%d"): x.index
        for x in CFGI.objects[
            : (NUM_OCCURRENCES * 12)
        ]  # CFGI_MAX=12w in client
    }

    cfgi = list()
    for x in days:
        try:
            cfgi.append(cfgi_values[x])
        except KeyError:
            cfgi.append(None)

    return dict(days=days, BTC=[btc_prices[x] for x in days], cfgi=cfgi,)


def get_chart_coin_or_token_frequency(coin_or_token, frequency):
    ref = s.EXCHANGES_AND_PAIRS_OF_REFERENCE["BTC"]
    ref_pair = ref["pair"]
    ref_exchange = ref["name"]

    model_history = type("History{}".format(frequency), (History,), {})
    rows = model_history.objects(
        symbol=coin_or_token + ref_pair, source=ref_exchange,
    )[:200]

    prices = list()
    volumes = list()
    num_trades = list()

    for x in rows:
        created_on_utc = x.created_on.replace(tzinfo=pytz.UTC)
        created_on_utc_ts = datetime.timestamp(created_on_utc) * 1000

        prices.append([created_on_utc_ts, float(x.price_usdt)])
        volumes.append([created_on_utc_ts, float(x.volume_24h)])
        num_trades.append([created_on_utc_ts, float(x.number_trades_24h)])

    prices.reverse()
    volumes.reverse()
    num_trades.reverse()

    return dict(prices=prices, volumes=volumes, num_trades=num_trades,)
