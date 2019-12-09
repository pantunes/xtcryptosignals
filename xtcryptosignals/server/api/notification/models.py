__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from mongoengine import (
    StringField,
    DecimalField,
    ReferenceField,
)
from xtcryptosignals.common.models import DocumentValidation
from xtcryptosignals.server.api.user.models import User
from xtcryptosignals.common.utils import get_coin_tokens
from xtcryptosignals.tasks import settings as s


class NotificationRule(DocumentValidation):
    coin_token = StringField(
        required=True, choices=get_coin_tokens(s.SYMBOLS_PER_EXCHANGE)
    )
    metric = StringField(required=True, choices=('price', 'volume',))
    interval = StringField(required=True, choices=s.HISTORY_FREQUENCY)
    percentage = DecimalField(required=True, precision=2)
    user = ReferenceField(User, required=True)

    meta = {
        'collection': 'notification_rule',
    }


class Notification(DocumentValidation):
    message = StringField(required=True)
    user = ReferenceField(User, required=True)

    meta = {
        'collection': 'notification',
        'ordering': ['-created_on'],
    }
