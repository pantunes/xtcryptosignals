__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import redis
import json
from marshmallow import Schema, fields
from xtcryptosignals.tasks import settings as s


red = redis.Redis.from_url(s.BROKER_URL)


class BaseSchema(Schema):
    ticker = fields.Str(required=True)
    price_usdt = fields.Float()

    def post_load(self, data):
        data_symbol = data["symbol"][-3:]
        if data_symbol in s.COIN_OR_TOKEN_REFERENCE["VAR"]:
            key = s.REDIS_KEY_TICKER.format(
                source=s.BINANCE,
                symbol=data_symbol + "USDT",
                frequency=s.HISTORY_FREQUENCY[0],
            )
            ser_row = red.get(key)
            if not ser_row:
                return
            deser_row = json.loads(ser_row)
            price = float(deser_row["price"])
            data["price_usdt"] = data["price"] * price
        elif data_symbol in s.COIN_OR_TOKEN_REFERENCE["STABLE"]:
            data["price_usdt"] = data["price"]
        elif data["symbol"][-4:] == s.COIN_OR_TOKEN_REFERENCE_DEFAULT:
            data["price_usdt"] = data["price"]
