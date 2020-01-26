__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from datetime import datetime, timedelta
from xtcryptosignals.tasks.models.history import History
from xtcryptosignals.tasks.models.cfgi import CFGI


NUM_LAST_DAYS_HISTORY = 30


def get_chart_fear_and_greed_index_and_btc():
    utcnow = datetime.utcnow()

    days = [
        (utcnow + timedelta(-x)).strftime("%Y-%m-%d")
        for x in range(NUM_LAST_DAYS_HISTORY, 1, -1)
    ]

    model_history = type('History1d', (History,), {})
    prices = model_history.objects(
        symbol='BTCUSDT',
        source='binance',
    )[:NUM_LAST_DAYS_HISTORY]
    btc_prices = {
        x.created_on.strftime("%Y-%m-%d"): int(x.price_usdt) for x in prices
    }

    cfgi = CFGI.objects[:30]
    cfgi_values = {x.added_on.strftime("%Y-%m-%d"): x.index for x in cfgi}

    return dict(
        days=days,
        btc=[btc_prices[x] for x in days],
        cfgi=[cfgi_values[x] for x in days],
    )
