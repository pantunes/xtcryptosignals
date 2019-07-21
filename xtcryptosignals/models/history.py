__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from mongoengine import (
    Document,
    StringField,
    DecimalField,
    IntField,
    ListField,
    DateTimeField
)
import xtcryptosignals.settings as s


class History(Document):
    symbol = StringField(required=True)
    source = StringField(required=True)
    price = DecimalField(required=True, precision=s.SYMBOL_FLOAT_PRECISION)
    number_trades_24h = IntField()
    volume_24h = DecimalField(precision=s.SYMBOL_FLOAT_PRECISION)
    price_change = DecimalField(precision=2)
    number_trades_change = DecimalField(precision=2)
    volume_change = DecimalField(precision=2)
    price_change_chart = ListField(
        DecimalField(required=True, precision=2)
    )
    created_on = DateTimeField(required=True)

    meta = {
        'abstract': True,
        'indexes': [
            ("-created_on", ),
            ("symbol", "source", ),
            ("symbol", "source", "-created_on", ),
        ],
        'ordering': ['-created_on'],
    }

    def get_object(self, frequency):
        item = dict(frequency=frequency)
        for k in self._fields.keys():
            if self[k] is None:
                continue
            if k == "id":
                continue
            if k in ['symbol', 'source', 'number_trades_24h']:
                item[k] = self[k]
                continue
            if k in ['price', 'volume_24h', 'price_change',
                     'number_trades_change', 'volume_change']:
                item[k] = float(self[k])
                continue
            if k in ['created_on']:
                item['updated_on'] = self[k].strftime('%Y-%m-%d %H:%M:%S')
                continue
            if k in ['price_change_chart']:
                item[k] = [float(x) for x in self[k]]
                continue
        return item
