__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import redis
from datetime import datetime, timedelta
from mongoengine import (
    StringField,
    DecimalField,
    IntField,
    DateTimeField,
)
from xtcryptosignals.common.models import (
    DocumentValidation,
    _set_timestamp,
)
from xtcryptosignals.tasks import settings as s
from xtcryptosignals.tasks.models.history import History
from xtcryptosignals.tasks.utils import convert_to_seconds


red = redis.Redis.from_url(s.BROKER_URL)


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


def _set_history(ticker):
    ticker.history_list_dicts = []
    for x in s.HISTORY_FREQUENCY:
        model_history = type('History{}'.format(x), (History,), {})

        row = model_history.objects(
            symbol=ticker['symbol'],
            source=ticker['source']
        ).first()

        number_trades_change = None
        price_change_prepared = None
        volume_change = None
        price_change_chart = []

        if row:
            price_change, number_trades_change, volume_change = \
                ticker._calculate_changes(row)
            price_change_prepared = _get_abs_zero(price_change)
            price_change_chart = _get_price_change_chart(
                row, price_change_prepared
            )

        history_object = model_history(
            symbol=ticker['symbol'],
            source=ticker['source'],
            ticker=ticker['ticker'],
            price=ticker['price'],
            number_trades_24h=ticker['number_trades_24h'],
            volume_24h=ticker['volume_24h'],
            price_change=price_change_prepared,
            number_trades_change=_get_abs_zero(
                number_trades_change),
            volume_change=_get_abs_zero(volume_change),
            price_change_chart=price_change_chart,
        )

        if 'price_usdt' in ticker:
            history_object.price_usdt = ticker['price_usdt']

        if not ticker._exists_row_offset(model_history, offset=x):
            history_object.save()
        else:
            _set_timestamp(history_object)

        # still emit this object ticker
        ticker.history_list_dicts.append(
            history_object.to_dict(frequency=x)
        )


def _save_ticker_in_redis(ticker):
    row = ticker.to_dict()
    red.set(s.REDIS_KEY_TICKER.format(**row), row['price'])


class Ticker(DocumentValidation):
    symbol = StringField(required=True)
    source = StringField(required=True)
    ticker = StringField(required=True)
    price = DecimalField(required=True, precision=s.SYMBOL_FLOAT_PRECISION)
    price_usdt = DecimalField(precision=s.SYMBOL_FLOAT_PRECISION)
    # 24h
    price_change_24h = DecimalField(precision=s.SYMBOL_FLOAT_PRECISION)
    lowest_price_24h = DecimalField(precision=s.SYMBOL_FLOAT_PRECISION)
    highest_price_24h = DecimalField(precision=s.SYMBOL_FLOAT_PRECISION)
    number_trades_24h = IntField()
    volume_24h = DecimalField(precision=s.SYMBOL_FLOAT_PRECISION)
    # dates
    opened_on = DateTimeField()
    closed_on = DateTimeField()

    _pre_save_hooks = (_set_history, _save_ticker_in_redis,)

    meta = {
        'collection': 'ticker',
        'ordering': ['-created_on'],
    }

    def to_dict(self):
        e = super(Ticker, self).to_dict().copy()
        for k in e:
            if k in (
                'price',
                'price_usdt',
                'price_change_24h',
                'lowest_price_24h',
                'highest_price_24h',
                'volume_24h',
            ):
                e[k] = float(self[k])
                continue
            if k in ('number_trades_24h',):
                e[k] = int(self[k])
                continue
            if k in ('opened_on', 'closed_on',):
                e[k] = self[k].strftime('%Y-%m-%d %H:%M:%S')
                continue
        return e

    def _exists_row_offset(self, model, offset):
        dt = datetime.utcnow() - timedelta(
            seconds=convert_to_seconds(offset) - 1.0
        )
        return model.objects(
            symbol=self['symbol'],
            source=self['source'],
            created_on__gte=dt
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

    history_list_dicts = []

    def get_history(self):
        return self.history_list_dicts
