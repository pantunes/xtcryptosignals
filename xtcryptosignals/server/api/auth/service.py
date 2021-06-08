__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import secrets
from mongoengine.errors import DoesNotExist, NotUniqueError
from xtcryptosignals.server.api.auth.models import Auth
from xtcryptosignals.server.api.user.models import UserTokenFavourites
from xtcryptosignals.server.api.projects.models import Project
from xtcryptosignals.server.api.user.service import get_user
from xtcryptosignals.server.crypto import Crypto
from xtcryptosignals.tasks import settings as s


def get_auth_with_token(token):
    try:
        auth = Auth.objects.get(token=token, active=True)
    except DoesNotExist:
        raise ValueError("Session is invalid.", 401)
    return auth


def login(data):
    user = get_user(data)
    if not user.active:
        raise ValueError("User account needs to be activated.", 403)
    try:
        auth = Auth.objects.get(user=user, active=True)
    except DoesNotExist:
        auth = Auth(user=user)
    auth.token = secrets.token_hex(128)
    try:
        auth.save()
    except NotUniqueError:
        raise ValueError("Session token is not unique.", 412)
    return auth


def logout(auth):
    auth.active = False
    auth.save()


def subscription(auth, data):
    auth.user.metadata.update(subscription=data)
    auth.user.save()


def exchange_binance_keys(auth, data, pkey):
    fkey = Crypto._get_fkey(key=pkey, salt=auth.user.salt)

    _data = data.copy()
    for key in data:
        _data[key] = Crypto.encrypt(fkey, data[key])

    auth.user.metadata.update(exchanges=dict(binance=_data))
    auth.user.save()


def get_user_coin_or_token_favourite(auth, coin_or_token):
    try:
        Project.objects.get(coin_or_token=coin_or_token)
    except DoesNotExist:
        raise ValueError("Coin or Token does not exist.", 405)
    try:
        return UserTokenFavourites.objects.get(
            user=auth.user, coin_token=coin_or_token
        )
    except DoesNotExist:
        raise ValueError("Coin or Token is not in favourites.", 204)


def toggle_user_coin_or_token_favourite(auth, coin_or_token):
    try:
        coin_or_token = get_user_coin_or_token_favourite(
            auth=auth, coin_or_token=coin_or_token
        )
        coin_or_token.delete()
    except ValueError as err:
        error, status = err.args
        if status == 405:
            raise ValueError(err)
        UserTokenFavourites.objects.create(
            user=auth.user, coin_token=coin_or_token
        )


def get_favourites(auth):
    favourites = {}
    for utfav in UserTokenFavourites.objects(user=auth.user):
        if utfav.coin_token not in s.EXCHANGES_AND_PAIRS_OF_REFERENCE:
            continue
        favourites[utfav.coin_token] = s.EXCHANGES_AND_PAIRS_OF_REFERENCE[
            utfav.coin_token
        ]
    return favourites
