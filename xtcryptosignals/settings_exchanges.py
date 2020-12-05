__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


# Exchanges
BINANCE = "binance"
BINANCE_DEX = "binance_dex"
UPHOLD = "uphold"
OKEX = "okex"
IDEX = "idex"
SWITCHEO = "switcheo"
HOTBIT = "hotbit"
BIBOX = "bibox"
OKCOIN = "okcoin"
BITHUMB = "bithumb"
COINBENE = "coinbene"
DCOIN = "dcoin"
BITMAX = "bitmax"
BILAXY = "bilaxy"
BITSTAMP = "bitstamp"
KUCOIN = "kucoin"
COINBASE_PRO = "coinbase_pro"
LIQUID = "liquid"


EXCHANGES = [
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
]


SYMBOLS_PER_EXCHANGE = []

# Binance
SYMBOLS_PER_EXCHANGE.append(
    {
        BINANCE: {
            "pairs": [
                ("BTC", "USDT"),
                ("BTC", "EUR"),
                ("ETH", "USDT"),
                ("ETH", "BTC"),
                ("ETH", "EUR"),
                ("LINK", "USDT"),
                ("LINK", "BTC"),
                ("XRP", "USDT"),
                ("LTC", "USDT"),
                ("XLM", "USDT"),
                ("XMR", "USDT"),
                ("REN", "USDT"),
                ("REN", "BTC"),
                ("KNC", "USDT"),
                ("KNC", "BTC"),
                ("AAVE", "USDT"),
                ("AAVE", "BTC"),
                ("UNI", "USDT"),
                ("UNI", "BTC"),
                ("DOT", "USDT"),
                ("DOT", "BTC"),
                ("BNB", "USDT"),
                ("BNB", "BTC"),
                ("ICX", "USDT"),
                ("VET", "USDT"),
                ("NANO", "USDT"),
                ("USDT", "DAI"),
                ("USDC", "USDT"),
                ("ADA", "USDT"),
                ("XTZ", "USDT"),
                ("LTO", "USDT"),
                ("LTO", "BTC"),
                ("FTM", "USDT"),
                ("FTM", "BTC"),
                ("ONT", "USDT"),
                ("HBAR", "USDT"),
                ("HBAR", "BTC"),
            ],
        }
    }
)

# Bitstamp
SYMBOLS_PER_EXCHANGE.append(
    {
        BITSTAMP: {
            "pairs": [
                ("BTC", "USD"),
                ("BTC", "EUR"),
                ("ETH", "USD"),
                ("ETH", "EUR"),
                ("LINK", "USD"),
                ("LINK", "EUR"),
                ("USDC", "USD"),
                ("USDC", "EUR"),
            ]
        }
    }
)

# OKEx
SYMBOLS_PER_EXCHANGE.append(
    {OKEX: {"pairs": [("BTC", "USDT"), ("ETH", "USDT"), ("LTC", "USDT"),]}}
)

# Coinbase Pro
SYMBOLS_PER_EXCHANGE.append(
    {
        COINBASE_PRO: {
            "pairs": [
                ("BTC", "USD"),
                ("BTC", "EUR"),
                ("ETH", "USD"),
                ("ETH", "EUR"),
                ("XLM", "USD"),
                ("UNI", "USD"),
                ("DAI", "USD"),
                ("NU", "USD"),
                ("NU", "EUR"),
            ]
        }
    }
)

# Kucoin
SYMBOLS_PER_EXCHANGE.append(
    {
        KUCOIN: {
            "pairs": [
                ("BTC", "USDT"),
                ("ETH", "USDT"),
                ("EWT", "BTC"),
                ("EWT", "USDT"),
            ]
        }
    }
)

# BIBOX
SYMBOLS_PER_EXCHANGE.append(
    {BIBOX: {"pairs": [("BTC", "USDT"), ("ETH", "USDT"), ("LTC", "USDT"),]}}
)

# Bitmax
SYMBOLS_PER_EXCHANGE.append(
    {
        BITMAX: {
            "pairs": [("LTO", "USDT"), ("LTO", "BTC"), ("BTMX", "USDT"),],
            "single_request": True,
        }
    }
)

# IDEX
SYMBOLS_PER_EXCHANGE.append({IDEX: {"pairs": []}})

# OKCoin
SYMBOLS_PER_EXCHANGE.append(
    {OKCOIN: {"pairs": [("BTC", "USD"), ("ETH", "USD"), ("LTC", "USD"),]}}
)

# LIQUID
SYMBOLS_PER_EXCHANGE.append(
    {LIQUID: {"pairs": [("EWT", "BTC"), ("EWT", "ETH"),]}}
)

# Coinbene
SYMBOLS_PER_EXCHANGE.append({COINBENE: {"pairs": []}})

# Hotbit
SYMBOLS_PER_EXCHANGE.append({HOTBIT: {"pairs": [], "single_request": True,}})

# Bilaxy
SYMBOLS_PER_EXCHANGE.append(
    {
        BILAXY: {
            "pairs": [("BTC", "USDT"), ("ETH", "USDT"),],
            "single_request": True,
        }
    }
)

# Uphold
SYMBOLS_PER_EXCHANGE.append(
    {UPHOLD: {"pairs": [("BTC", "USD"), ("ETH", "USD"), ("LTC", "USD"),]}}
)

# Binance DEX
SYMBOLS_PER_EXCHANGE.append(
    {BINANCE_DEX: {"pairs": [("LTO", "BNB"),], "single_request": True,}}
)

# DCoin
SYMBOLS_PER_EXCHANGE.append({DCOIN: {"pairs": [], "single_request": True,}})

# Switcheo
SYMBOLS_PER_EXCHANGE.append({SWITCHEO: {"pairs": [], "single_request": True,}})


EXCHANGES_AND_PAIRS_OF_REFERENCE = {
    "BTC": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT"]},
    },
    "ETH": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC"]},
    },
    "LINK": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC"]},
    },
    "XRP": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT"]},
    },
    "LTC": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT"]},
    },
    "BNB": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT"]},
    },
    "XLM": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT"]},
    },
    "USDC": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT"]},
    },
    "USDT": {
        "pair": "DAI",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["DAI"]},
    },
    "DAI": {"pair": "USD", "name": COINBASE_PRO,},
    "LTO": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC"]},
    },
    "FTM": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC"]},
    },
    "EWT": {"pair": "USDT", "name": KUCOIN,},
    "ADA": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT"]},
    },
    "XTZ": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT"]},
    },
    "KNC": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC"]},
    },
    "AAVE": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC"]},
    },
    "UNI": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC"]},
    },
    "REN": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC"]},
    },
    "DOT": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC"]},
    },
    "NU": {"pair": "USD", "name": COINBASE_PRO,},
    "XMR": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT"]},
    },
    "VET": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT"]},
    },
    "ICX": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT"]},
    },
    "NANO": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT"]},
    },
    "ONT": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT"]},
    },
    "HBAR": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC"]},
    },
    "BTMX": {"pair": "USDT", "name": BITMAX,},
}

# Check to make sure that ALL configured symbols must have an
# exchange and pair referenced
from xtcryptosignals.common.utils import get_coin_tokens  # noqa: E402

tokens_and_coins = get_coin_tokens(SYMBOLS_PER_EXCHANGE)
tokens_and_coins_ref = sorted(list(EXCHANGES_AND_PAIRS_OF_REFERENCE.keys()))
assert (
    tokens_and_coins == tokens_and_coins_ref
), f"\n{tokens_and_coins}\n{tokens_and_coins_ref}"
