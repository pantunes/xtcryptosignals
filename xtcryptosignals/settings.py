__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


TICKER_SCHEDULE = 10  # executed each X seconds

# mongodb collections created during runtime
HISTORY_FREQUENCY = (
    str(TICKER_SCHEDULE) + "s",
    "1m",
    "10m",
    "30m",
    "1h",
    "4h",
    "12h",
    "1d",
    "1w",
    "4w",
    "12w",
    "24w",
    "1y",
)

PRICE_CHANGE_FREQUENCIES = (
    "1h",
    "1d",
    "1w",
    "4w",
)

# exchanges settings
from xtcryptosignals.settings_exchanges import (
    EXCHANGES,
    SYMBOLS_PER_EXCHANGE,
    EXCHANGES_AND_PAIRS_OF_REFERENCE,
    BINANCE,
    BINANCE_DEX,
    UPHOLD,
    OKEX,
    IDEX,
    SWITCHEO,
    HOTBIT,
    BIBOX,
    OKCOIN,
    BITHUMB,
    COINBENE,
    DCOIN,
    BITMAX,
    BILAXY,
    BITSTAMP,
    KUCOIN,
    COINBASE_PRO,
    LIQUID,
)  # noqa

__all__ = [
    "EXCHANGES",
    "SYMBOLS_PER_EXCHANGE",
    "EXCHANGES_AND_PAIRS_OF_REFERENCE",
    "TICKER_SCHEDULE",
    "HISTORY_FREQUENCY",
    "PRICE_CHANGE_FREQUENCIES",
    # exchanges
    "BINANCE",
    "BINANCE_DEX",
    "UPHOLD",
    "OKEX",
    "IDEX",
    "SWITCHEO",
    "HOTBIT",
    "BIBOX",
    "OKCOIN",
    "BITHUMB",
    "COINBENE",
    "DCOIN",
    "BITMAX",
    "BILAXY",
    "BITSTAMP",
    "KUCOIN",
    "COINBASE_PRO",
    "LIQUID",
]
