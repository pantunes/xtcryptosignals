__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from mongoengine.errors import ValidationError
from xtcryptosignals.server.api.transaction.models import Transaction
from xtcryptosignals.server.utils import _sanitize_errors_mongoengine


def add_transaction(auth, data):
    data.update(user=auth.user)

    transaction = Transaction(**data)
    try:
        transaction.save()
    except ValidationError as err:
        error = _sanitize_errors_mongoengine(err)
        raise ValueError(error, 406)


def transactions(auth):
    return Transaction.objects(user=auth.user)
