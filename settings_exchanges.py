__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__version__ = "1.0"
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

SYMBOLS_PER_EXCHANGE = list()

# Binance
SYMBOLS_PER_EXCHANGE.append({
    BINANCE: {
        'pairs': [
            ('BTC', 'USDT'),
            ('ETH', 'USDT'),
            ('LTC', 'USDT'),
            ('NEO', 'USDT'),
            ('ICX', 'USDT'),
            ('XRP', 'USDT'),
            ('ONT', 'USDT'),
            ('NANO', 'BTC'),
            ('POA', 'BTC'),
            ('ZRX', 'BTC'),
            ('GAS', 'BTC'),
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

# OKEx
SYMBOLS_PER_EXCHANGE.append({
    OKEX: {
        'pairs': [
            ('BTC', 'USDT'),
            ('ETH', 'USDT'),
            ('LTC', 'USDT'),
            ('XRP', 'USDT'),
        ]
    }
})

# IDEX
SYMBOLS_PER_EXCHANGE.append({
    IDEX: {
        'pairs': [
            ('AUC', 'ETH'),
        ]
    }
})

# SWITCHEO
SYMBOLS_PER_EXCHANGE.append({
    SWITCHEO: {
        'single_request': True,
        'pairs': [
            ('SDS', 'NEO'),
            ('NOS', 'NEO'),
        ]
    }
})

# HOTBIT
SYMBOLS_PER_EXCHANGE.append({
    HOTBIT: {
        'single_request': True,
        'pairs': [
            ('NOS', 'BTC'),
            ('NOS', 'ETH'),
        ]
    }
})

# BIBOX
SYMBOLS_PER_EXCHANGE.append({
    BIBOX: {
        'pairs': [
            ('BTC', 'USDT'),
        ]
    }
})
