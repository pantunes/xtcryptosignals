__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from mongoengine.errors import ValidationError, DoesNotExist
from xtcryptosignals.server.api.notifications.models import (
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


def edit_notification_rule(auth, notification, data):
    data.update(user=auth.user)

    try:
        notification_rule = NotificationRule.objects.get(
            pk=notification, user=auth.user
        )
    except DoesNotExist:
        raise ValueError("This record does not exist.", 406)

    try:
        notification_rule.update(**data)
    except ValidationError as err:
        error = _sanitize_errors_mongoengine(err)
        raise ValueError(error, 406)
    # TODO: a little work-around
    notification_rule.save()


def get_notification_rule(auth, notification):
    try:
        notification_rule = NotificationRule.objects.get(
            pk=notification, user=auth.user
        )
    except DoesNotExist:
        raise ValueError("This record does not exist.", 406)
    return notification_rule


def delete_notification_rule(auth, notification):
    try:
        notification_rule = NotificationRule.objects.get(
            pk=notification, user=auth.user
        )
    except DoesNotExist:
        raise ValueError("This record does not exist.", 406)

    notification_rule.delete()


def notifications(auth, coin_token):
    kwargs = dict(user=auth.user)
    if coin_token != "ALL":
        kwargs.update(coin_token=coin_token)
    return Notification.objects(**kwargs)


def notification_coin_tokens(auth):
    return Notification.objects(user=auth.user).distinct("coin_token")


def notification_rules(auth):
    return NotificationRule.objects(user=auth.user)
