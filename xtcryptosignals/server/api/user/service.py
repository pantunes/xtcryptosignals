__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import bcrypt
from mongoengine.errors import (
    NotUniqueError,
    ValidationError,
    DoesNotExist,
)
from xtcryptosignals.server.api.user.models import User


def create_user(data):
    data['password'] = bcrypt.hashpw(
        data['password'].encode(), bcrypt.gensalt()
    )

    del data['confirm_password']

    user = User(**data)

    try:
        user.save()
    except NotUniqueError:
        raise ValueError(
            'User account already exists ({email}).'.format(**data), 409
        )
    except ValidationError as err:
        from xtcryptosignals.server.utils import _sanitize_errors_mongoengine
        error = _sanitize_errors_mongoengine(err)
        raise ValueError(error, 406)
    return user


def get_user(data, authenticate=True):
    try:
        user = User.objects.get(email=data['email'])
    except DoesNotExist:
        raise ValueError('Bad credentials.', 404)
    if authenticate:
        if not bcrypt.checkpw(
            data['password'].encode(), user.password.encode()
        ):
            raise ValueError('Bad credentials.', 404)
    return user
