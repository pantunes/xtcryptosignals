__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import secrets
from mongoengine.errors import DoesNotExist, NotUniqueError
from xtcryptosignals.server.api.auth.models import Auth
from xtcryptosignals.server.api.user.service import get_user


def get_auth_with_token(token):
    try:
        auth = Auth.objects.get(token=token, active=True)
    except DoesNotExist:
        raise ValueError('Session is invalid.', 401)
    return auth


def login(data):
    user = get_user(data)
    if not user.active:
        raise ValueError('User account needs to be activated.', 403)
    try:
        auth = Auth.objects.get(user=user, active=True)
    except DoesNotExist:
        auth = Auth(user=user)
    auth.token = secrets.token_hex(128)
    try:
        auth.save()
    except NotUniqueError:
        raise ValueError('Session token is not unique.', 412)
    return auth


def logout(auth):
    auth.active = False
    auth.save()


def subscription(auth, data):
    auth.user.metadata.update(subscription=data)
    auth.user.save()
