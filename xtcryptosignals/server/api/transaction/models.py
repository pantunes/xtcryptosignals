__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from mongoengine import (
    StringField,
    DecimalField,
    ReferenceField,
    DateField,
)
from xtcryptosignals.server.api.user.models import User
from xtcryptosignals.common.models import DocumentValidation
from xtcryptosignals.common.utils import get_coin_tokens
from xtcryptosignals.tasks import settings as s


class Transaction(DocumentValidation):
    coin_token = StringField(
        required=True, choices=get_coin_tokens(s.SYMBOLS_PER_EXCHANGE)
    )
    units = DecimalField(required=True, precision=s.SYMBOL_FLOAT_PRECISION)
    amount = DecimalField(required=True, precision=s.SYMBOL_FLOAT_PRECISION)
    user = ReferenceField(User, required=True)
    added_on = DateField(required=True)
    in_or_out = StringField(required=True, choices=('in', 'out',))

    meta = {
        'collection': 'transaction',
    }
