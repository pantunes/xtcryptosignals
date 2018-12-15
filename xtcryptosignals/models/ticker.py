__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from datetime import datetime, timedelta
from mongoengine import (
    Document,
    StringField,
    DecimalField,
    IntField,
    DateTimeField,
)
from mongoengine.queryset.visitor import Q
import xtcryptosignals.settings as s
from xtcryptosignals.models.history import History
from xtcryptosignals.utils.helpers import convert_to_seconds


class Ticker(Document):
    symbol = StringField(required=True)
    source = StringField(required=True)
    price = DecimalField(required=True, precision=s.SYMBOL_FLOAT_PRECISION)
    # 24h
    price_change_24h_percent = DecimalField(precision=s.SYMBOL_FLOAT_PRECISION)
    lowest_price_24h = DecimalField(precision=s.SYMBOL_FLOAT_PRECISION)
    highest_price_24h = DecimalField(precision=s.SYMBOL_FLOAT_PRECISION)
    number_trades_24h = IntField()
    volume_24h = DecimalField(precision=s.SYMBOL_FLOAT_PRECISION)
    # dates
    opened_on = DateTimeField()
    closed_on = DateTimeField()
    created_on = DateTimeField(required=True, default=datetime.utcnow)

    meta = {
        'collection': 'ticker',
        'indexes': [
            ("-created_on", ),
        ],
        'ordering': ['-created_on'],
    }

    def save(self, *args, **kwargs):
        for x in s.HISTORY_FREQUENCY:
            model = type('History{}'.format(x), (History,), {})
            dt = datetime.utcnow() - timedelta(
                seconds=convert_to_seconds(x) - 1.0
            )
            row = model.objects(
                Q(symbol=self['symbol']) &
                Q(source=self['source']) &
                Q(created_on__gte=dt)
            ).first()

            if not row:
                row = model.objects(
                    symbol=self['symbol'],
                    source=self['source']
                ).first()

                number_trades_change_percent = None
                price_change_percent = None
                volume_change_percent = None
                if row:
                    price_change_percent = (float(
                        self['price']/row.price
                    ) - 1.0) * 100.0
                    if round(price_change_percent, 2) == -0.00:
                        price_change_percent = 0.0
                    if self['number_trades_24h']:
                        number_trades_change_percent = (float(
                            self['number_trades_24h']/row.number_trades_24h
                        ) - 1.0) * 100.0
                        if round(number_trades_change_percent, 2) == -0.00:
                            number_trades_change_percent = 0.0
                    if self['volume_24h']:
                        volume_change_percent = (float(
                            self['volume_24h']/row.volume_24h
                        ) - 1.0) * 100.0
                        if round(volume_change_percent, 2) == -0.00:
                            volume_change_percent = 0.0
                m = model(
                    symbol=self['symbol'],
                    source=self['source'],
                    price=self['price'],
                    number_trades_24h=self['number_trades_24h'],
                    volume_24h=self['volume_24h'],
                    price_change_percent=price_change_percent,
                    number_trades_change_percent=number_trades_change_percent,
                    volume_change_percent=volume_change_percent,
                    created_on=self['created_on'],
                )
                m.save()
        return super(Ticker, self).save(*args, **kwargs)

    def get_object(self):
        item = {}
        for k in self._fields.keys():
            if k == "id":
                continue
            if k in ['symbol', 'source', 'price']:
                item[k] = self[k]
                continue
            if k in ['created_on']:
                item[k] = str(self[k])
                continue
        return item
