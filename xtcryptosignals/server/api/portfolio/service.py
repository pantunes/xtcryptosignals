__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from xtcryptosignals.server.api.transaction.models import Transaction
from xtcryptosignals.common.utils import get_coin_tokens
from xtcryptosignals.tasks import settings as s


def portfolio(auth):
    portf = dict()

    for coin_token in get_coin_tokens(s.SYMBOLS_PER_EXCHANGE):
        total_units = Transaction.objects(
            user=auth.user, coin_token=coin_token
        ).sum('units')

        if total_units == 0:
            continue

        total_amount_paid = Transaction.objects(
            user=auth.user, coin_token=coin_token
        ).sum('amount_paid')

        average_paid = total_amount_paid / total_units

        portf.update({
            coin_token: dict(
                total_units=total_units,
                total_amount_paid=total_amount_paid,
                average_paid=average_paid
            )
        })

    return portf
