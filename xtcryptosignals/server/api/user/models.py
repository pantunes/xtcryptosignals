__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from mongoengine import (
    StringField,
    BooleanField,
    DictField,
    EmailField,
)
from xtcryptosignals.common.models import DocumentValidation


class User(DocumentValidation):
    name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    metadata = DictField()
    active = BooleanField(default=True)

    meta = {
        'collection': 'user',
    }
