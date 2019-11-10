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
        # TODO: Improve
        symbol = 'ETHUSDT'
        _id = '{}_{}'.format(s.BINANCE, symbol)
        if data['source'] == s.BINANCE and data['symbol'] == symbol:
            red.set(_id, data['price'])
            return data
        elif data['symbol'][-3:] != 'ETH':
            return data
        ethusdt = red.get(_id)
        if ethusdt:
            data['price_usdt'] = data['price'] * float(ethusdt)
        return data
