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
from mongoengine import (
    StringField,
    DecimalField,
    IntField,
    ListField,
)
from xtcryptosignals.common.models import DocumentValidation
from xtcryptosignals.tasks import settings as s


red = redis.Redis.from_url(s.BROKER_URL)


class History(DocumentValidation):
    symbol = StringField(required=True)
    source = StringField(required=True)
    ticker = StringField(required=True)
    price = DecimalField(required=True, precision=s.SYMBOL_FLOAT_PRECISION)
    price_usdt = DecimalField(precision=s.SYMBOL_FLOAT_PRECISION)
    number_trades_24h = IntField()
    volume_24h = DecimalField(precision=s.SYMBOL_FLOAT_PRECISION)
    price_change = DecimalField(precision=2)
    number_trades_change = DecimalField(precision=2)
    volume_change = DecimalField(precision=2)
    price_change_chart = ListField(DecimalField(required=True, precision=2))

    meta = {
        "abstract": True,
        "indexes": [
            {"fields": ("symbol", "source", "-created_on",), "unique": True}
        ],
        "ordering": ["-created_on"],
    }

    def to_dict(self, frequency):
        e = super().to_dict().copy()
        for k in e:
            if k in (
                "price",
                "price_usdt",
                "volume_24h",
                "price_change",
                "number_trades_change",
                "volume_change",
            ):
                e[k] = float(self[k])
                continue
            if k in ["price_change_chart"]:
                e[k] = [float(x) for x in self[k]]
                continue
        e["frequency"] = frequency
        e["updated_on"] = e["created_on"]

        for x in s.PRICE_CHANGE_FREQUENCIES:
            key = s.REDIS_KEY_TICKER.format(
                source=self.source, symbol=self.symbol, frequency=x,
            )
            try:
                ser_row = red.get(key)
                deser_row = json.loads(ser_row)
                price_change = float(deser_row["price"])
                pc = (float(self.price) - price_change) / price_change
                # return 0.0 if -0.0
                e[f"price_change_{x}"] = round((pc * 100) + 0.0, 2)
            except (TypeError, ZeroDivisionError):
                e[f"price_change_{x}"] = None
        return e

    @staticmethod
    def get_ticker_data_from_namespace(namespace):
        rows = []
        for x in s.SYMBOLS_PER_EXCHANGE:
            for exchange, items in x.items():
                for symbol in [x[0] + x[1] for x in items["pairs"]]:
                    key = s.REDIS_KEY_TICKER.format(
                        source=exchange, symbol=symbol, frequency=namespace[1:],
                    )
                    ser_row = red.get(key)
                    if not ser_row:
                        continue
                    deser_row = json.loads(ser_row)
                    rows.append(deser_row)
        return rows
