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
from xtcryptosignals.server.api.transactions.models import Transaction
from xtcryptosignals.common.utils import get_coin_tokens
from xtcryptosignals.tasks import settings as s


red = redis.Redis.from_url(s.BROKER_URL)


def get_exchange_for(coin_token):
    return s.EXCHANGES_AND_PAIRS_OF_REFERENCE[coin_token]


def _get_percentage(x, y):
    try:
        t = -(100 - ((x * 100) / y))
        return round(t, 2)
    except ZeroDivisionError:
        return 0.0


def _get_current_price(exchange, coin_token):
    key = s.REDIS_KEY_TICKER.format(
        source=exchange["name"],
        symbol=coin_token + exchange["pair"],
        frequency=s.HISTORY_FREQUENCY[0],
    )
    ser_row = red.get(key)
    deser_row = json.loads(ser_row)
    price = float(deser_row["price"])

    if exchange["pair"] != "USDT":
        key = s.REDIS_KEY_TICKER.format(
            source=s.BINANCE,
            symbol=exchange["pair"] + "USDT",
            frequency=s.HISTORY_FREQUENCY[0],
        )
        ser_row = red.get(key)
        deser_row = json.loads(ser_row)
        price_usdt = float(deser_row["price"])

        price = price * price_usdt

    return price


def _set_share_per_coin_token(p):
    total_paid = p["total_paid"]

    for coin_or_token, struct in p["coin_tokens"].items():
        p["coin_tokens"][coin_or_token].update(
            {"share": round(struct["amount"] * 100 / total_paid, 2),}
        )


def portfolio(auth):
    _portfolio = dict(coin_tokens=dict())
    total_paid = 0
    total_value = 0
    for coin_token in get_coin_tokens(s.SYMBOLS_PER_EXCHANGE):

        total_units_in = Transaction.objects(
            user=auth.user, coin_token=coin_token, in_or_out="in"
        ).sum("units")

        if total_units_in == 0:
            continue

        total_units_out = Transaction.objects(
            user=auth.user, coin_token=coin_token, in_or_out="out"
        ).sum("units")

        total_amount_paid = Transaction.objects(
            user=auth.user, coin_token=coin_token, in_or_out="in"
        ).sum("amount")

        total_amount_received = Transaction.objects(
            user=auth.user, coin_token=coin_token, in_or_out="out"
        ).sum("amount")

        total_units = total_units_in - total_units_out

        if total_units == 0:
            continue

        total_amount = total_amount_paid - total_amount_received

        average_paid = total_amount / total_units

        exchange = get_exchange_for(coin_token)

        try:
            current_price = _get_current_price(exchange, coin_token)
        except TypeError:
            # pair is not stored in Redis - most likely Exchange API is
            # failing
            # TODO: Still display this row in red in UI
            continue

        _portfolio["coin_tokens"].update(
            {
                coin_token: dict(
                    exchange=exchange,
                    current_price=round(
                        current_price, s.SYMBOL_FLOAT_PRECISION
                    ),
                    units=round(total_units, s.SYMBOL_FLOAT_PRECISION),
                    amount=total_amount,
                    average_paid=average_paid,
                    balance=round((current_price - average_paid) * total_units),
                    position=_get_percentage(current_price, average_paid),
                ),
            }
        )

        total_paid += total_amount

        total_value += total_units * current_price

    btc_price = _portfolio["coin_tokens"]["BTC"]["current_price"]

    _portfolio.update(
        total_paid=round(total_paid, 2),
        total_value=round(total_value, 2),
        total_position=_get_percentage(total_value, total_paid),
        total_in_btc=round(total_value / btc_price, 2),
    )

    _set_share_per_coin_token(_portfolio)

    return _portfolio
