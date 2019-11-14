__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import redis
from xtcryptosignals.server.api.transaction.models import Transaction
from xtcryptosignals.common.utils import get_coin_tokens
from xtcryptosignals.tasks import settings as s


red = redis.Redis.from_url(s.BROKER_URL)


def get_exchange_for(coin_token):
    return s.EXCHANGES_OF_REFERENCE[coin_token]


def _get_total_position(x, y):
    if x >= y:
        t = (100 - ((y * 100) / x))
    else:
        t = -(100 - ((x * 100) / y))
    return round(t, 2)


def _get_total_value(exchange, coin_token, total_units):
    key = s.REDIS_KEY_TICKER.format(
        source=exchange['name'],
        symbol=coin_token + exchange['pair']
    )
    price = float(red.get(key))

    if exchange['pair'] != 'USDT':
        price_usdt = float(red.get(
            s.REDIS_KEY_TICKER.format(
                source=s.BINANCE,
                symbol=exchange['pair'] + 'USDT'
            )
        ))
        price = price * price_usdt

    return total_units * price


def portfolio(auth):
    _portfolio = dict(coin_tokens=dict())
    total_paid = 0
    total_value = 0
    for coin_token in get_coin_tokens(s.SYMBOLS_PER_EXCHANGE):

        total_units_in = Transaction.objects(
            user=auth.user, coin_token=coin_token, in_or_out='in'
        ).sum('units')

        if total_units_in == 0:
            continue

        total_units_out = Transaction.objects(
            user=auth.user, coin_token=coin_token, in_or_out='out'
        ).sum('units')

        total_amount_paid = Transaction.objects(
            user=auth.user, coin_token=coin_token, in_or_out='in'
        ).sum('amount')

        total_amount_received = Transaction.objects(
            user=auth.user, coin_token=coin_token, in_or_out='out'
        ).sum('amount')

        total_units = total_units_in - total_units_out
        total_amount = total_amount_paid - total_amount_received

        average_paid = total_amount / total_units

        exchange = get_exchange_for(coin_token)

        _portfolio['coin_tokens'].update({
            coin_token: dict(
                exchange=exchange,
                total_units=total_units,
                total_amount=total_amount,
                average_paid=average_paid,
            ),
        })

        total_paid += total_amount

        total_value += _get_total_value(exchange, coin_token, total_units)

    _portfolio.update(
        total_paid=round(total_paid, 2),
        total_value=round(total_value, 2),
        total_position=_get_total_position(total_value, total_paid),
    )

    return _portfolio
