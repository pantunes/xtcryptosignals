__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import os


try:
    DEBUG = bool(int(os.environ['DEBUG']))
except KeyError:
    # development
    DEBUG = True

MONGODB_NAME = 'XTCryptoSignals'

TICKER_SCHEDULE = 10  # executed each X seconds
TIMEOUT_PER_SYMBOL_REQUEST = 2.0  # in seconds
TIMEOUT_PER_SYMBOLS_REQUEST = 5.0  # in seconds
SYMBOL_FLOAT_PRECISION = 8

# mongodb collections created during runtime
HISTORY_FREQUENCY = (
    str(TICKER_SCHEDULE) + 's', '30s', '1m', '3m', '5m', '15m', '30m', '45m',
    '1h', '2h', '3h', '4h', '12h', '1d', '4d', '1w', '2w', '4w', '12w', '24w',
    '1y',
)

# local settings
from xtcryptosignals.settings_local import (
    IP_ADDRESS, PORT_SERVER, PORT_CLIENT,
    SERVER_API_BASE_URL,
    BINANCE_API_KEY,
    BINANCE_API_SECRET,
)  # noqa

# exchanges settings
from xtcryptosignals.settings_exchanges import (
    EXCHANGES, SYMBOLS_PER_EXCHANGE,
    BINANCE, UPHOLD, OKEX, IDEX, SWITCHEO, HOTBIT, BIBOX, OKCOIN,
    BITHUMB, COINBENE,
)  # noqa

__all__ = [
    'IP_ADDRESS', 'PORT_SERVER', 'PORT_CLIENT', 'SERVER_API_BASE_URL',
    'BINANCE_API_KEY', 'BINANCE_API_SECRET', 'EXCHANGES',
    'SYMBOLS_PER_EXCHANGE', 'BINANCE', 'UPHOLD', 'OKEX', 'IDEX', 'SWITCHEO',
    'HOTBIT', 'BIBOX', 'OKCOIN', 'BITHUMB', 'COINBENE',
]
