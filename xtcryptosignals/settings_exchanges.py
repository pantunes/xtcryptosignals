__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


# Exchanges
BINANCE = 'binance'
UPHOLD = 'uphold'
OKEX = 'okex'
IDEX = 'idex'
SWITCHEO = 'switcheo'
HOTBIT = 'hotbit'
BIBOX = 'bibox'
OKCOIN = 'okcoin'
BITHUMB = 'bithumb'
COINBENE = 'coinbene'
DCOIN = 'dcoin'
BITMAX = 'bitmax'
BILAXY = 'bilaxy'


EXCHANGES = [
    BINANCE, UPHOLD, OKEX, IDEX, SWITCHEO, HOTBIT,
    BIBOX, OKCOIN, BITHUMB, COINBENE, DCOIN, BITMAX,
    BILAXY,
]

SYMBOLS_PER_EXCHANGE = list()

# Binance
SYMBOLS_PER_EXCHANGE.append({
    BINANCE: {
        'pairs': [
            ('BTC', 'USDT'),
            ('ETH', 'USDT'),
            ('LTC', 'USDT'),
        ]
    }
})

# OKEx
SYMBOLS_PER_EXCHANGE.append({
    OKEX: {
        'pairs': [
            ('BTC', 'USDT'),
            ('ETH', 'USDT'),
            ('LTC', 'USDT'),
        ]
    }
})

# IDEX
SYMBOLS_PER_EXCHANGE.append({
    IDEX: {
        'pairs': [
            ('LTO', 'ETH'),
        ]
    }
})

# BIBOX
SYMBOLS_PER_EXCHANGE.append({
    BIBOX: {
        'pairs': [
            ('BTC', 'USDT'),
            ('ETH', 'USDT'),
            ('LTC', 'USDT'),
        ]
    }
})

# OKCoin
SYMBOLS_PER_EXCHANGE.append({
    OKCOIN: {
        'pairs': [
            ('BTC', 'USD'),
            ('ETH', 'USD'),
            ('LTC', 'USD'),
        ]
    }
})

# Coinbene
SYMBOLS_PER_EXCHANGE.append({
    COINBENE: {
        'pairs': [
            ('BTC', 'USDT'),
            ('ETH', 'USDT'),
            ('LTC', 'USDT'),
        ]
    }
})

# Uphold
SYMBOLS_PER_EXCHANGE.append({
    UPHOLD: {
        'pairs': [
            ('BTC', 'USD'),
            ('ETH', 'USD'),
            ('LTC', 'USD'),
        ]
    }
})

# DCoin
SYMBOLS_PER_EXCHANGE.append({
    DCOIN: {
        'pairs': [
            ('LTO', 'USDT'),
        ],
        'single_request': True,
    }
})

# Bitmax
SYMBOLS_PER_EXCHANGE.append({
    BITMAX: {
        'pairs': [
            ('LTO', 'USDT'),
            ('LTO', 'BTC'),
        ],
        'single_request': True,
    }
})

# Hotbit
SYMBOLS_PER_EXCHANGE.append({
    HOTBIT: {
        'pairs': [
            ('LTO', 'USDT'),
            ('LTO', 'BTC'),
            ('LTO', 'ETH'),
        ],
        'single_request': True,
    }
})

# Bilaxy
SYMBOLS_PER_EXCHANGE.append({
    BILAXY: {
        'pairs': [
            ('LTO', 'ETH'),
            ('BTC', 'USDT'),
            ('ETH', 'USDT'),
        ],
        'single_request': True,
    }
})

# Switcheo
SYMBOLS_PER_EXCHANGE.append({
    SWITCHEO: {
        'pairs': [
        ],
        'single_request': True,
    }
})
