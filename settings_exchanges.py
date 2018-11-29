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
ETH = 'ETH'
NEO = 'NEO'
GAS = 'GAS'

BINANCE = 'binance'
UPHOLD = 'uphold'
OKEX = 'okex'
IDEX = 'idex'
SWITCHEO = 'switcheo'


EXCHANGES_AND_SYMBOLS = list()

# Binance
EXCHANGES_AND_SYMBOLS.append({
    BINANCE: {
        'pairs': [
            (BTC, USDT),
            (ETH, USDT),
            ('LTC', USDT),
            (NEO, USDT),
            ('ICX', USDT),
            ('XRP', USDT),
            ('ONT', USDT),
            ('NANO', BTC),
            ('POA', BTC),
            ('ZRX', BTC),
            (GAS, BTC),
        ]
    }
})

# Uphold
EXCHANGES_AND_SYMBOLS.append({
    UPHOLD: {
        'pairs': [
            (BTC, USD),
            (ETH, USD),
            ('LTC', USD),
            ('XRP', USD),
        ]
    }
})

# OKEx
EXCHANGES_AND_SYMBOLS.append({
    OKEX: {
        'pairs': [
            (BTC, USDT),
            (ETH, USDT),
            ('LTC', USDT),
            ('XRP', USDT),
        ]
    }
})

# IDEX
EXCHANGES_AND_SYMBOLS.append({
    IDEX: {
        'pairs': [
            ('AUC', ETH),
        ]
    }
})

# SWITCHEO
EXCHANGES_AND_SYMBOLS.append({
    SWITCHEO: {
        'single_request': True,
        'pairs': [
            ('SDS', NEO),
            ('NOS', NEO),
        ]
    }
})
