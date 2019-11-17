__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from mongoengine import (
    StringField,
    EmailField,
)
from xtcryptosignals.common.models import DocumentValidation


class Contact(DocumentValidation):
    email = EmailField(required=True)
    reason = StringField(required=True, choices=('question', 'bug',))
    message = StringField(required=True)
