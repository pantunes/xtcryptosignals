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


def _get_abs_zero(f):
    try:
        return 0.0 if round(f, 2) == -0.00 else f
    except TypeError:
        return f


def _get_price_change_chart(row, price_change):
    x = row.price_change_chart
    x.append(price_change)
    x.reverse()
    x = x[:s.PRICES_CHANGE_CHART_SIZE]
    x.reverse()
    return x


class Ticker(Document):
    symbol = StringField(required=True)
    source = StringField(required=True)
    price = DecimalField(required=True, precision=s.SYMBOL_FLOAT_PRECISION)
    # 24h
    price_change_24h = DecimalField(precision=s.SYMBOL_FLOAT_PRECISION)
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

    def _exists_row_offset(self, model, offset):
        dt = datetime.utcnow() - timedelta(
            seconds=convert_to_seconds(offset) - 1.0
        )
        return model.objects(
            Q(symbol=self['symbol']) &
            Q(source=self['source']) &
            Q(created_on__gte=dt)
        ).first()

    def _calculate_changes(self, row):
        number_trades_change = None
        volume_change = None
        try:
            price_change = (float(
                self['price'] / row.price
            ) - 1.0) * 100.0
        except ZeroDivisionError:
            price_change = 1.0
        if self['number_trades_24h']:
            try:
                number_trades_change = (float(
                    self['number_trades_24h'] / row.number_trades_24h
                ) - 1.0) * 100.0
            except ZeroDivisionError:
                number_trades_change = 1.0
        if self['volume_24h']:
            try:
                volume_change = (float(
                    self['volume_24h'] / row.volume_24h
                ) - 1.0) * 100.0
            except ZeroDivisionError:
                volume_change = 1.0
        return price_change, number_trades_change, volume_change

    def save(self, *args, **kwargs):
        history_list_dicts = []
        for x in s.HISTORY_FREQUENCY:
            model = type('History{}'.format(x), (History,), {})

            row = model.objects(
                symbol=self['symbol'],
                source=self['source']
            ).first()

            number_trades_change = None
            price_change_prepared = None
            volume_change = None
            price_change_chart = []

            if row:
                price_change, number_trades_change, volume_change = \
                    self._calculate_changes(row)
                price_change_prepared = _get_abs_zero(price_change)
                price_change_chart = _get_price_change_chart(
                    row, price_change_prepared
                )

            history_object = model(
                symbol=self['symbol'],
                source=self['source'],
                price=self['price'],
                number_trades_24h=self['number_trades_24h'],
                volume_24h=self['volume_24h'],
                price_change=price_change_prepared,
                number_trades_change=_get_abs_zero(
                    number_trades_change),
                volume_change=_get_abs_zero(volume_change),
                price_change_chart=price_change_chart,
                created_on=self['created_on'],
            )

            if not self._exists_row_offset(model, offset=x):
                history_object.save()

            history_list_dicts.append(
                history_object.get_object(frequency=x)
            )

        super(Ticker, self).save(*args, **kwargs)
        return history_list_dicts
