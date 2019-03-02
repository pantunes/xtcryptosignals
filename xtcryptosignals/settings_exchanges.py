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


EXCHANGES = [
    BINANCE, UPHOLD, OKEX, IDEX, SWITCHEO, HOTBIT,
    BIBOX, OKCOIN, BITHUMB, COINBENE
]

SYMBOLS_PER_EXCHANGE = list()

# Binance
SYMBOLS_PER_EXCHANGE.append({
    BINANCE: {
        'pairs': [
            ('BTC', 'USDT'),
            ('ETH', 'USDT'),
            ('LTC', 'USDT'),
            ('XRP', 'USDT'),
            ('NEO', 'USDT'),
            ('ONT', 'USDT'),
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
            ('XRP', 'USDT'),
            ('NEO', 'USDT'),
            ('ONT', 'USDT'),
        ]
    }
})

# IDEX
SYMBOLS_PER_EXCHANGE.append({
    IDEX: {
        'pairs': [
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
            ('NEO', 'USDT'),
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
            ('XRP', 'USD'),
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
            ('XRP', 'USDT'),
            ('NEO', 'USDT'),
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
            ('XRP', 'USD'),
        ]
    }
})

# SWITCHEO
SYMBOLS_PER_EXCHANGE.append({
    SWITCHEO: {
        'pairs': [
        ],
        'single_request': True,
    }
})

# HOTBIT
SYMBOLS_PER_EXCHANGE.append({
    HOTBIT: {
        'pairs': [
        ],
        'single_request': True,
    }
})
