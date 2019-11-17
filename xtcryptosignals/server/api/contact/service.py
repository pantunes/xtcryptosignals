__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from mongoengine.errors import ValidationError
from xtcryptosignals.server.api.contact.models import Contact


def save_contact(data):
    contact = Contact(**data)
    try:
        contact.save()
    except ValidationError as err:
        from xtcryptosignals.server.utils import _sanitize_errors_mongoengine
        error = _sanitize_errors_mongoengine(err)
        raise ValueError(error, 406)
