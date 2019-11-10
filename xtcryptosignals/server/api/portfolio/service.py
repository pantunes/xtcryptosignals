__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from xtcryptosignals.server.api.transaction.models import Transaction
from xtcryptosignals.common.utils import get_coin_tokens
from xtcryptosignals.tasks import settings as s


def get_exchange_for(coin_token):
    return s.EXCHANGES_OF_REFERENCE[coin_token]


def portfolio(auth):
    _portfolio = dict(coin_tokens=dict())
    _spent = 0
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

        _portfolio['coin_tokens'].update({
            coin_token: dict(
                exchange=get_exchange_for(coin_token),
                total_units=total_units,
                total_amount=total_amount,
                average_paid=average_paid,
            ),
        })

        _spent += total_amount

    _portfolio.update(
        total_spent=_spent,
    )

    return _portfolio
