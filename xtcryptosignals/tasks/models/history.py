__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from mongoengine import (
    StringField,
    DecimalField,
    IntField,
    ListField,
)
from xtcryptosignals.common.models import DocumentValidation
from xtcryptosignals.tasks import settings as s


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
        'abstract': True,
        'indexes': [
            ("symbol", "source", ),
            ("symbol", "source", "-created_on", ),
        ],
        'ordering': ['-created_on'],
    }

    def to_dict(self, frequency):
        e = super(History, self).to_dict().copy()
        for k in e:
            if k in (
                'price',
                'price_usdt',
                'volume_24h',
                'price_change',
                'number_trades_change',
                'volume_change',
            ):
                e[k] = float(self[k])
                continue
            if k in ['price_change_chart']:
                e[k] = [float(x) for x in self[k]]
                continue
        e['frequency'] = frequency
        e['updated_on'] = e['created_on']
        return e

    @staticmethod
    def get_ticker_data_from_namespace(namespace):
        model_history = type('History{}'.format(namespace[1:]), (History,), {})
        rows = []
        for x in s.SYMBOLS_PER_EXCHANGE:
            for exchange, items in x.items():
                for symbol in [x[0] + x[1] for x in items['pairs']]:
                    row = model_history.objects(
                        symbol=symbol,
                        source=exchange
                    ).first()
                    if not row:
                        continue
                    rows.append(row.to_dict(frequency=namespace[1:]))
        return rows
