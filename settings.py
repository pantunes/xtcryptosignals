__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


MONGODB_NAME = 'XTCryptoSignals'

TICKER_SCHEDULE = 10.0  # each X seconds
TIMEOUT_PER_SYMBOL = 0.5  # in seconds
SYMBOL_FLOAT_PRECISION = 8

HISTORY_FREQUENCY = (
    '10s', '30s', '1m', '10m', '30m', '1h', '3h', '6h', '12h', '24h'
)

# local settings
from settings_local import (
    BINANCE_API_KEY,
    BINANCE_API_SECRET,
)  # noqa

# exchanges settings
from settings_exchanges import (
    USD, BTC, USDT,
    BINANCE, UPHOLD, OKEX, IDEX,
    EXCHANGES_AND_SYMBOLS,
)  # noqa

__all__ = [
    'BINANCE_API_KEY', 'BINANCE_API_SECRET', 'USD',
    'BTC', 'USDT', 'BINANCE', 'UPHOLD', 'OKEX', 'IDEX',
    'EXCHANGES_AND_SYMBOLS',
]
