__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


# Exchanges
BINANCE = 'binance'
BINANCE_DEX = 'binance_dex'
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
    BINANCE, BINANCE_DEX, UPHOLD, OKEX, IDEX, SWITCHEO, HOTBIT,
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
            ('BNB', 'USDT'),
            ('XRP', 'USDT'),
            ('XLM', 'USDT'),
            ('XMR', 'USDT'),
            ('ADA', 'USDT'),
            ('XTZ', 'USDT'),
            ('ICX', 'USDT'),
            ('VET', 'USDT'),
            ('NANO', 'USDT'),
            ('ONT', 'USDT'),
        ],
    }
})

# Binance DEX
SYMBOLS_PER_EXCHANGE.append({
    BINANCE_DEX: {
        'pairs': [
            ('LTO', 'BNB'),
        ],
        'single_request': True,
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
            ('LQD', 'ETH'),
            ('IDEX', 'ETH'),
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

# Bitmax
SYMBOLS_PER_EXCHANGE.append({
    BITMAX: {
        'pairs': [
            ('LTO', 'USDT'),
            ('LTO', 'BTC'),
            ('LTO', 'ETH'),
            ('BTMX', 'USDT'),
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
            ('LQD', 'ETH'),
            ('LQD', 'BTC'),
            ('CARD', 'ETH'),
        ],
        'single_request': True,
    }
})

# Bilaxy
SYMBOLS_PER_EXCHANGE.append({
    BILAXY: {
        'pairs': [
            ('BTC', 'USDT'),
            ('ETH', 'USDT'),
            ('LQD', 'ETH'),
        ],
        'single_request': True,
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


EXCHANGES_AND_PAIRS_OF_REFERENCE = {
    'BTC': {
        'pair': 'USDT',
        'name': BINANCE,
    },
    'ETH': {
        'pair': 'USDT',
        'name': BINANCE,
    },
    'LTC': {
        'pair': 'USDT',
        'name': BINANCE,
    },
    'BNB': {
        'pair': 'USDT',
        'name': BINANCE,
    },
    'XRP': {
        'pair': 'USDT',
        'name': BINANCE,
    },
    'XLM': {
        'pair': 'USDT',
        'name': BINANCE,
    },
    'XMR': {
        'pair': 'USDT',
        'name': BINANCE,
    },
    'ADA': {
        'pair': 'USDT',
        'name': BINANCE,
    },
    'VET': {
        'pair': 'USDT',
        'name': BINANCE,
    },
    'ICX': {
        'pair': 'USDT',
        'name': BINANCE,
    },
    'XTZ': {
        'pair': 'USDT',
        'name': BINANCE,
    },
    'NANO': {
        'pair': 'USDT',
        'name': BINANCE,
    },
    'ONT': {
        'pair': 'USDT',
        'name': BINANCE,
    },
    'BTMX': {
        'pair': 'USDT',
        'name': BITMAX,
    },
    'LTO': {
        'pair': 'USDT',
        'name': BITMAX,
    },
    'IDEX': {
        'pair': 'ETH',
        'name': IDEX,
    },
    'LQD': {
        'pair': 'ETH',
        'name': BILAXY,
    },
    'CARD': {
        'pair': 'ETH',
        'name': HOTBIT,
    },
}
