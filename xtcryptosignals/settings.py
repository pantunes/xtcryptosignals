__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import os


IP_ADDRESS = '0.0.0.0'
PORT_SERVER = 5000
PORT_CLIENT = 8000

try:
    DEBUG = bool(int(os.environ['DEBUG']))
except KeyError:
    # development
    DEBUG = True

try:
    SERVER_API_BASE_URL = os.environ['SERVER_API_BASE_URL']
except KeyError:
    # development
    SERVER_API_BASE_URL = 'http://127.0.0.1:{}/'.format(PORT_SERVER)

MONGODB_NAME = 'XTCryptoSignals'

TICKER_SCHEDULE = 10  # executed each X seconds
TIMEOUT_PER_SYMBOL_REQUEST = 2.0  # in seconds
TIMEOUT_PER_SYMBOLS_REQUEST = 5.0  # in seconds
SYMBOL_FLOAT_PRECISION = 8
PRICES_CHANGE_CHART_SIZE = 6

# mongodb collections created during runtime
HISTORY_FREQUENCY = (
    str(TICKER_SCHEDULE) + 's', '30s', '1m', '10m', '30m',
    '1h', '4h', '12h', '1d', '4d', '1w', '4w', '12w', '24w',
    '1y',
)

# local settings
from xtcryptosignals.settings_local import (
    BINANCE_API_KEY,
    BINANCE_API_SECRET,
)  # noqa

# exchanges settings
from xtcryptosignals.settings_exchanges import (
    EXCHANGES, SYMBOLS_PER_EXCHANGE,
    BINANCE, BINANCE_DEX, UPHOLD, OKEX, IDEX, SWITCHEO, HOTBIT, BIBOX, OKCOIN,
    BITHUMB, COINBENE, DCOIN, BITMAX, BILAXY,
)  # noqa

__all__ = [
    'BINANCE_API_KEY', 'BINANCE_API_SECRET', 'EXCHANGES',
    'SYMBOLS_PER_EXCHANGE', 'BINANCE', 'BINANCE_DEX', 'UPHOLD', 'OKEX',
    'IDEX', 'SWITCHEO', 'HOTBIT', 'BIBOX', 'OKCOIN', 'BITHUMB', 'COINBENE',
    'DCOIN', 'BITMAX', 'BILAXY',
]
