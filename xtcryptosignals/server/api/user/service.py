__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import bcrypt
from mongoengine.errors import NotUniqueError, ValidationError
from xtcryptosignals.server.api.user.models import User


def create_user(data):
    data['password'] = bcrypt.hashpw(
        data['password'].encode(), bcrypt.gensalt()
    )

    user = User(**data)

    try:
        user.save()
    except NotUniqueError:
        raise ValueError(
            'User account already exists ({email}).'.format(**data), 409
        )
    except ValidationError:
        raise ValueError(
            'Invalid e-mail address ({email}).'.format(**data), 406
        )
    return user
