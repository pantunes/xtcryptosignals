__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from mongoengine import (
    DecimalField,
    IntField,
)
from xtcryptosignals.common.models import DocumentValidation


class Tether(DocumentValidation):
    total_supply_eth = DecimalField(required=True, precision=2)
    num_holders_eth = IntField()

    meta = {
        "collection": "tether",
        "indexes": [("-created_on",),],
        "ordering": ["-created_on"],
    }
