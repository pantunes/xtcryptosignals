__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


USD = 'USD'
USDT = 'USDT'
BTC = 'BTC'

BINANCE = 'binance'
UPHOLD = 'uphold'
OKEX = 'okex'

# Binance
EXCHANGES_AND_SYMBOLS = {
    BINANCE: {
        'BTC': USDT,
        'ETH': USDT,
        'LTC': USDT,
        'NEO': USDT,
        'ICX': USDT,
        'XRP': USDT,
        'ONT': USDT,
        'NANO': BTC,
        'POA': BTC,
        'ZRX': BTC,
    }
}

# Uphold
EXCHANGES_AND_SYMBOLS.update({
    UPHOLD: {
        'BTC': USD,
        'ETH': USD,
        'LTC': USD,
        'XRP': USD,
    }
})

# OKEx
EXCHANGES_AND_SYMBOLS.update({
    OKEX: {
        'BTC-': USDT,
        'ETH-': USDT,
        'LTC-': USDT,
        'XRP-': USDT,
    }
})
