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
                ("BTC", "BUSD"),
                ("BTC", "EUR"),
                ("ETH", "USDT"),
                ("ETH", "BUSD"),
                ("ETH", "BTC"),
                ("ETH", "EUR"),
                ("LINK", "USDT"),
                ("LINK", "BUSD"),
                ("LINK", "BTC"),
                ("XRP", "USDT"),
                ("XRP", "BTC"),
                ("LTC", "USDT"),
                ("LTC", "BTC"),
                ("XLM", "USDT"),
                ("XLM", "BTC"),
                ("XMR", "USDT"),
                ("XMR", "BTC"),
                ("REN", "USDT"),
                ("REN", "BTC"),
                ("KNC", "USDT"),
                ("KNC", "BTC"),
                ("KNC", "BUSD"),
                ("AAVE", "USDT"),
                ("AAVE", "BTC"),
                ("UNI", "USDT"),
                ("UNI", "BTC"),
                ("UNI", "BUSD"),
                ("DOT", "USDT"),
                ("DOT", "BUSD"),
                ("DOT", "BTC"),
                ("ICP", "USDT"),
                ("ICP", "BTC"),
                ("BNB", "USDT"),
                ("BNB", "BUSD"),
                ("BNB", "BTC"),
                ("ICX", "USDT"),
                ("ICX", "BTC"),
                ("VET", "USDT"),
                ("VET", "BTC"),
                ("XNO", "USDT"),
                ("XNO", "BTC"),
                ("USDT", "DAI"),
                ("USDC", "USDT"),
                ("ADA", "USDT"),
                ("ADA", "BTC"),
                ("XTZ", "USDT"),
                ("XTZ", "BTC"),
                ("LTO", "USDT"),
                ("LTO", "BTC"),
                ("LTO", "BUSD"),
                ("FTM", "USDT"),
                ("FTM", "BUSD"),
                ("FTM", "BTC"),
                ("ALGO", "USDT"),
                ("ALGO", "BUSD"),
                ("ALGO", "BTC"),
                ("SOL", "USDT"),
                ("SOL", "BUSD"),
                ("SOL", "BTC"),
                ("ATOM", "USDT"),
                ("ATOM", "BUSD"),
                ("ATOM", "BTC"),
                ("WOO", "USDT"),
                ("WOO", "BTC"),
                ("WOO", "BUSD"),
                ("NEAR", "USDT"),
                ("NEAR", "BTC"),
                ("NEAR", "BUSD"),
                ("AVAX", "USDT"),
                ("AVAX", "BTC"),
                ("AVAX", "BUSD"),
                ("ONT", "USDT"),
                ("ONT", "BTC"),
                ("HBAR", "USDT"),
                ("HBAR", "BTC"),
                ("SNX", "USDT"),
                ("SNX", "BTC"),
                ("RLC", "USDT"),
                ("RLC", "BUSD"),
                ("RLC", "BTC"),
                ("BUSD", "USDT"),
            ],
            "single_request": True,
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

# Coinbase Pro
SYMBOLS_PER_EXCHANGE.append(
    {
        COINBASE_PRO: {
            "pairs": [
                ("BTC", "USD"),
                ("ETH", "USD"),
                ("DAI", "USD"),
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
    {
        BIBOX: {
            "pairs": [
                ("BTC", "USDT"),
                ("ETH", "USDT"),
                ("LTC", "USDT"),
            ]
        }
    }
)

# OKCoin
SYMBOLS_PER_EXCHANGE.append(
    {
        OKCOIN: {
            "pairs": [
                ("BTC", "USD"),
                ("ETH", "USD"),
                ("LTC", "USD"),
                ("USDT", "USD"),
            ]
        }
    }
)

# LIQUID
SYMBOLS_PER_EXCHANGE.append(
    {
        LIQUID: {
            "pairs": [
                ("EWT", "BTC"),
                ("EWT", "ETH"),
            ]
        }
    }
)

# Uphold
SYMBOLS_PER_EXCHANGE.append(
    {
        UPHOLD: {
            "pairs": [
                ("BTC", "USD"),
                ("ETH", "USD"),
                ("LTC", "USD"),
            ]
        }
    }
)

# Deprecated/Upgraded APIs #######

# OKEx
SYMBOLS_PER_EXCHANGE.append({OKEX: {"pairs": []}})


# EMPTY EXCHANGES (LOW VOLUME) #######

# IDEX
SYMBOLS_PER_EXCHANGE.append({IDEX: {"pairs": []}})

# Coinbene
SYMBOLS_PER_EXCHANGE.append({COINBENE: {"pairs": []}})

# Bitmax
SYMBOLS_PER_EXCHANGE.append(
    {
        BITMAX: {
            "pairs": [],
            "single_request": True,
        }
    }
)

# Hotbit
SYMBOLS_PER_EXCHANGE.append(
    {
        HOTBIT: {
            "pairs": [],
            "single_request": True,
        }
    }
)

# Bilaxy
SYMBOLS_PER_EXCHANGE.append(
    {
        BILAXY: {
            "pairs": [],
            "single_request": True,
        }
    }
)

# Binance DEX
SYMBOLS_PER_EXCHANGE.append(
    {
        BINANCE_DEX: {
            "pairs": [],
            "single_request": True,
        }
    }
)

# DCoin
SYMBOLS_PER_EXCHANGE.append(
    {
        DCOIN: {
            "pairs": [],
            "single_request": True,
        }
    }
)

# Switcheo
SYMBOLS_PER_EXCHANGE.append(
    {
        SWITCHEO: {
            "pairs": [],
            "single_request": True,
        }
    }
)

EXCHANGES_AND_PAIRS_OF_REFERENCE = {
    "BTC": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BUSD", "EUR"]},
    },
    "ETH": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC", "BUSD"]},
    },
    "LINK": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC"]},
    },
    "XRP": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC"]},
    },
    "LTC": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC"]},
    },
    "BNB": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC"]},
    },
    "XLM": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC"]},
    },
    "LTO": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC", "BUSD"]},
    },
    "ICP": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC"]},
    },
    "SOL": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC", "BUSD"]},
    },
    "ATOM": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC", "BUSD"]},
    },
    "FTM": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC", "BUSD"]},
        "is_defi": True,
    },
    "ALGO": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC", "BUSD"]},
    },
    "WOO": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC", "BUSD"]},
    },
    "NEAR": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC", "BUSD"]},
    },
    "AVAX": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC", "BUSD"]},
    },
    "EWT": {
        "pair": "USDT",
        "name": KUCOIN,
    },
    "RLC": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC"]},
    },
    "SNX": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC"]},
        "is_defi": True,
    },
    "KNC": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC"]},
        "is_defi": True,
    },
    "AAVE": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC"]},
        "is_defi": True,
    },
    "UNI": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC"]},
        "is_defi": True,
    },
    "REN": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC"]},
        "is_defi": True,
    },
    "DOT": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC"]},
    },
    "ADA": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC"]},
    },
    "XTZ": {
        "pair": "USDT",
        "name": BINANCE,
    },
    "XMR": {
        "pair": "USDT",
        "name": BINANCE,
    },
    "VET": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC"]},
    },
    "ICX": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC"]},
    },
    "XNO": {
        "pair": "USDT",
        "name": BINANCE,
    },
    "ONT": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC"]},
    },
    "HBAR": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT", "BTC"]},
    },
    "USDC": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT"]},
        "is_stable": True,
    },
    "USDT": {
        "pair": "USD",
        "name": OKCOIN,
        "is_stable": True,
    },
    "BUSD": {
        "pair": "USDT",
        "name": BINANCE,
        "market_depth": {"exchange": BINANCE, "pairs": ["USDT"]},
        "is_stable": True,
    },
    "DAI": {
        "pair": "USD",
        "name": COINBASE_PRO,
        "is_stable": True,
    },
}

# Settings validations

# Check to make sure that ALL configured symbols must have an
# exchange and pair referenced
from xtcryptosignals.common.utils import get_coin_tokens  # noqa: E402

tokens_and_coins = get_coin_tokens(SYMBOLS_PER_EXCHANGE)
tokens_and_coins_ref = sorted(list(EXCHANGES_AND_PAIRS_OF_REFERENCE.keys()))
assert (
    tokens_and_coins == tokens_and_coins_ref
), f"\n{tokens_and_coins}\n{tokens_and_coins_ref}"
