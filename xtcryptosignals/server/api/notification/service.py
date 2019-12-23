__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from mongoengine.errors import ValidationError
from xtcryptosignals.server.api.notification.models import (
    Notification,
    NotificationRule,
)
from xtcryptosignals.server.utils import _sanitize_errors_mongoengine


def add_notification_rule(auth, data):
    data.update(user=auth.user)

    notification_rule = NotificationRule(**data)
    try:
        notification_rule.save()
    except ValidationError as err:
        error = _sanitize_errors_mongoengine(err)
        raise ValueError(error, 406)


def notifications(auth, coin_token):
    kwargs = dict(user=auth.user)
    if coin_token != 'ALL':
        kwargs.update(coin_token=coin_token)
    return Notification.objects(**kwargs)


def notification_coin_tokens(auth):
    return Notification.objects(user=auth.user).distinct('coin_token')


def notification_rules(auth):
    return NotificationRule.objects(user=auth.user)
