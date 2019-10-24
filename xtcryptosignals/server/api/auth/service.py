__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import bcrypt
import secrets
from mongoengine.errors import DoesNotExist, NotUniqueError
from xtcryptosignals.server.api.auth.models import Auth
from xtcryptosignals.server.api.user.models import User


def get_user(data, authenticate=True):
    try:
        user = User.objects.get(email=data['email'])
    except DoesNotExist:
        raise ValueError('User not found ({email}).'.format(**data), 404)
    if authenticate:
        if not bcrypt.checkpw(
            data['password'].encode(), user.password.encode()
        ):
            raise ValueError('Bad credentials.', 404)
    return user


def get_auth_with_token(token):
    try:
        auth = Auth.objects.get(token=token)
    except DoesNotExist:
        raise ValueError('Session is invalid.', 401)
    return auth


def login(data):
    user = get_user(data)
    if not user.active:
        raise ValueError('User account needs to be activated.', 403)
    try:
        auth = Auth.objects.get(user=user)
    except DoesNotExist:
        auth = Auth(user=user)
    auth.token = secrets.token_hex(64)
    try:
        auth.save()
    except NotUniqueError:
        raise ValueError('Session token is not unique.', 412)
    return auth
