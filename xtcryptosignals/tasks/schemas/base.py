__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import redis
from marshmallow import (
    Schema,
    fields
)
from xtcryptosignals.tasks import settings as s


red = redis.Redis.from_url(s.BROKER_URL)


class BaseSchema(Schema):
    ticker = fields.Str(required=True)
    price_usdt = fields.Float()

    def post_load(self, data):
        data_symbol = data['symbol'][-3:]
        if data_symbol in ('ETH', 'BTC'):
            price = red.get(s.REDIS_KEY_TICKER.format(
                source=s.BINANCE,
                symbol=data_symbol + 'USDT'
            ))
            if not price:
                return
            data['price_usdt'] = data['price'] * float(price)
        elif data['symbol'][-4:] == 'USDT':
            data['price_usdt'] = data['price']
