__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from environs import Env


env = Env()
env.read_env(env("SETTINGS_APP"), recurse=False)


MONGODB_NAME = env.str("MONGODB_NAME")
MONGODB_HOST = env.str("MONGODB_HOST")
MONGODB_PORT = env.int("MONGODB_PORT")

WEBSITE_ADDRESS = env.str("WEBSITE_ADDRESS")

BROKER_URL = env.str("BROKER_URL")

CREATE_MODEL_TICKER = env.bool("CREATE_MODEL_TICKER")

ORDER_BOOK_SCHEDULE = 6.0  # executed each X seconds
TIMEOUT_ORDER_BOOK = ORDER_BOOK_SCHEDULE * 2.5

SYMBOL_FLOAT_PRECISION = 8
PRICES_CHANGE_CHART_SIZE = 12

REDIS_KEY_TICKER = "{source}_{symbol}_{frequency}_price"
REDIS_CFGI = "cfgi"

URL_CFGI = "https://api.alternative.me/fng"

VAPID_CLAIMS = env.str("VAPID_CLAIMS")
VAPID_PRIVATE_KEY = env.str("VAPID_PRIVATE_KEY")

ETHERSCAN_API_KEY = env.str("ETHERSCAN_API_KEY")

TELEGRAM_BOT_TOKEN = env.str("TELEGRAM_BOT_TOKEN")
TELEGRAM_GROUP_CHAT_ID = env.str("TELEGRAM_GROUP_CHAT_ID")

STATIC_COINS_TOKENS_LOGOS_FOLDER = "/static/imgs/logos/"

COIN_OR_TOKEN_REFERENCE = {
    "VAR": (
        "ETH",
        "BTC",
    ),
    "STABLE": (
        "DAI",
        "USD",
        "BUSD",
        "USDT",
    ),
}
COIN_OR_TOKEN_REFERENCE_DEFAULT = "USDT"

from xtcryptosignals.settings import *  # noqa
from xtcryptosignals.tasks.settings_local import *  # noqa

TIMEOUT_PER_SYMBOL_REQUEST = TICKER_SCHEDULE * 0.4
# Binance can have many pairs with a single call, timeout should be increased, just in case
TIMEOUT_PER_SYMBOLS_REQUEST = TICKER_SCHEDULE * 2.5

# Settings validations
assert TIMEOUT_PER_SYMBOL_REQUEST < TIMEOUT_PER_SYMBOLS_REQUEST

for _, x in EXCHANGES_AND_PAIRS_OF_REFERENCE.items():
    assert (
        x["pair"]
        in COIN_OR_TOKEN_REFERENCE["VAR"] + COIN_OR_TOKEN_REFERENCE["STABLE"]
    )

assert COIN_OR_TOKEN_REFERENCE_DEFAULT in COIN_OR_TOKEN_REFERENCE["STABLE"]
