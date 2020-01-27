__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from xtcryptosignals.tasks.models.history import History
from xtcryptosignals.tasks.models.cfgi import CFGI


NUM_OCCURRENCES = 30


def get_chart_fear_and_greed_index_and_btc(frequency):
    model_history = type('History{}'.format(frequency), (History,), {})
    prices = model_history.objects(
        symbol='BTCUSDT',
        source='binance',
    )[:NUM_OCCURRENCES]

    btc_prices = {
        x.created_on.strftime("%Y-%m-%d"): int(x.price_usdt) for x in prices
    }

    days = [x.created_on.strftime("%Y-%m-%d") for x in prices]
    days.reverse()

    cfgi_values = {
        x.added_on.strftime("%Y-%m-%d"): x.index for x in CFGI.objects
    }

    return dict(
        days=days,
        btc=[btc_prices[x] for x in days],
        cfgi=[cfgi_values[x] for x in days],
    )
