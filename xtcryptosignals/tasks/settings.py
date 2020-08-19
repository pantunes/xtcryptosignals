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

ORDER_BOOK_SCHEDULE = 3.0  # executed each X seconds
TIMEOUT_ORDER_BOOK = ORDER_BOOK_SCHEDULE * 0.8

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

from xtcryptosignals.settings import *  # noqa
from xtcryptosignals.tasks.settings_local import *  # noqa

TIMEOUT_PER_SYMBOL_REQUEST = TICKER_SCHEDULE * 0.4
TIMEOUT_PER_SYMBOLS_REQUEST = TICKER_SCHEDULE * 0.8

assert (
    TIMEOUT_PER_SYMBOL_REQUEST < TIMEOUT_PER_SYMBOLS_REQUEST < TICKER_SCHEDULE
)
assert TIMEOUT_ORDER_BOOK < ORDER_BOOK_SCHEDULE
