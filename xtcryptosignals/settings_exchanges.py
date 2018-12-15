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


SYMBOLS_PER_EXCHANGE = list()

# Binance
SYMBOLS_PER_EXCHANGE.append({
    BINANCE: {
        'pairs': [
            ('BTC', 'USDT'),
            ('XRP', 'USDT'),
            ('XRP', 'BTC'),
            ('ZIL', 'BTC'),
            ('ZIL', 'ETH'),
            ('VET', 'USDT'),
            ('VET', 'BTC'),
            ('VET', 'ETH'),
            ('ZEC', 'BTC'),
            ('NEO', 'USDT'),
            ('NEO', 'BTC'),
            ('BNB', 'BTC'),
            ('BNB', 'USDT'),
            ('BNB', 'ETH'),
            ('XMR', 'BTC'),
            ('XMR', 'ETH'),
            ('ETH', 'USDT'),
            ('ETH', 'BTC'),
            ('NANO', 'BTC'),
            ('NANO', 'ETH'),
            ('NANO', 'BNB'),
            ('ICX', 'USDT'),
            ('ICX', 'BTC'),
            ('ICX', 'ETH'),
            ('GAS', 'BTC'),
            ('QLC', 'BTC'),
            ('QLC', 'ETH'),
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
            ('XRP', 'USDT'),
            ('XRP', 'BTC'),
            ('ZIL', 'USDT'),
            ('ZIL', 'BTC'),
            ('ONT', 'USDT'),
            ('ONT', 'BTC'),
            ('LTC', 'USDT'),
            ('LTC', 'BTC'),
            ('ETH', 'USDT'),
            ('ETH', 'BTC'),
            ('NANO', 'USDT'),
            ('NANO', 'BTC'),
            ('ICX', 'USDT'),
            ('ICX', 'BTC'),
            ('GAS', 'BTC'),
            ('GAS', 'USDT'),
            ('GAS', 'ETH'),
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
            ('ONT', 'USDT'),
            ('ONT', 'BTC'),
            ('ONT', 'ETH'),
            ('NEO', 'USDT'),
            ('NEO', 'BTC'),
            ('NEO', 'ETH'),
            ('LTC', 'USDT'),
            ('LTC', 'BTC'),
            ('CARD', 'ETH'),
        ]
    }
})

# SWITCHEO
SYMBOLS_PER_EXCHANGE.append({
    SWITCHEO: {
        'pairs': [
            ('NOS', 'NEO'),
            ('SOUL', 'NEO'),
            ('AUC', 'ETH'),
        ],
        'single_request': True,
    }
})

# HOTBIT
SYMBOLS_PER_EXCHANGE.append({
    HOTBIT: {
        'pairs': [
            ('NOS', 'ETH'),
            ('NOS', 'BTC'),
            ('SOUL', 'BTC'),
            ('SOUL', 'ETH'),
            ('CARD', 'BTC'),
            ('CARD', 'ETH'),
            ('LQD', 'BTC'),
            ('LQD', 'ETH'),
        ],
        'single_request': True,
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
            ('ZEC', 'USD'),
        ]
    }
})

# Bithumb
SYMBOLS_PER_EXCHANGE.append({
    BITHUMB: {
        'pairs': [
            ('XMR', 'KRW'),
            ('ZEC', 'KRW'),
            ('BTC', 'KRW'),
            ('XRP', 'KRW'),
            ('ETH', 'KRW'),
        ]
    }
})

# Coinbene
SYMBOLS_PER_EXCHANGE.append({
    COINBENE: {
        'pairs': [
            ('BTC', 'USDT'),
        ]
    }
})
