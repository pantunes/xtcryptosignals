__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from mongoengine.errors import ValidationError
from xtcryptosignals.server.api.transaction.models import Transaction


def add_transaction(auth, data):
    data.update(user=auth.user)

    transaction = Transaction(**data)
    try:
        transaction.save()
    except ValidationError:
        raise ValueError(
            'Coin/Token is invalid ({coin_token}).'.format(**data), 406
        )


def transactions(auth):
    return Transaction.objects(user=auth.user)
