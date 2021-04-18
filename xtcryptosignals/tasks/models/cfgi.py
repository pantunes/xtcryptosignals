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
    DateField,
)
from xtcryptosignals.common.models import DocumentValidation


class CFGI(DocumentValidation):
    index = IntField(required=True)
    added_on = DateField(required=True)

    meta = {
        "collection": "fear_and_greed_index",
        "indexes": [
            ("-added_on",),
        ],
        "ordering": ["-added_on"],
    }
