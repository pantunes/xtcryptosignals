__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from mongoengine import (
    IntField,
    StringField,
    DictField,
    ListField,
    DateField,
    BooleanField,
)
from xtcryptosignals.common.models import DocumentValidation


class Event(DocumentValidation):
    title = StringField(required=True)
    tickers = ListField(StringField(required=True))
    categories = ListField(StringField(required=True))
    can_occur_before = BooleanField(required=True)
    json_id = IntField(required=True)
    json = DictField(required=True)
    happening_on = DateField(required=True)

    meta = {
        "collection": "event",
        "indexes": [("-happening_on",), ],
        "ordering": ["-happening_on"],
    }
