__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from mongoengine import (
    StringField,
    BooleanField,
    DictField,
    EmailField,
    ReferenceField,
)
from xtcryptosignals.common.models import DocumentValidation
from xtcryptosignals.common.utils import get_coin_tokens
from xtcryptosignals.tasks import settings as s


class User(DocumentValidation):
    name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    metadata = DictField()
    active = BooleanField(default=True)

    meta = {
        "collection": "user",
    }

    @property
    def salt(self):
        return f"{self.pk}.{self.email}.{self.password}.{self.created_on}"


class UserTokenFavourites(DocumentValidation):
    coin_token = StringField(
        required=True, choices=get_coin_tokens(s.SYMBOLS_PER_EXCHANGE)
    )
    user = ReferenceField(User, required=True)

    meta = {
        "collection": "user_token_favourites",
        "indexes": [
            {
                "fields": (
                    "coin_token",
                    "user",
                ),
                "unique": True,
            }
        ],
    }
