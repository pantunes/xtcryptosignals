__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from xtcryptosignals.server.api.transaction.models import Transaction
from xtcryptosignals.common.utils import get_coin_tokens
from xtcryptosignals.tasks import settings as s


def get_preferred_exchange(coin_token):
    for pref_exchange in s.EXCHANGES_OF_PREFERENCE:
        for x in s.SYMBOLS_PER_EXCHANGE:
            for exchange, items in x.items():
                if exchange == pref_exchange:
                    for symbol in [x[0] + x[1] for x in items['pairs']]:
                        if symbol == coin_token + 'USDT':
                            return exchange.upper()
    raise ValueError(
        'Exchange of Preference not set to {}USDT'.format(coin_token)
    )


def portfolio(auth):
    _portfolio = dict()

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

        _portfolio.update({
            coin_token: dict(
                exchange=get_preferred_exchange(coin_token),
                total_units=total_units,
                total_amount_paid=total_amount_paid,
                average_paid=average_paid,
            ),
        })

    return _portfolio
