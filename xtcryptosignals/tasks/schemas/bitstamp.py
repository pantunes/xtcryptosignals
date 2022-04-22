__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from marshmallow import (
    fields,
    pre_load,
    post_load,
)

from xtcryptosignals.tasks import settings as s
from xtcryptosignals.tasks.schemas.base import BaseSchema


class Bitstamp(BaseSchema):
    symbol = fields.Str(required=True)
    source = fields.Str(required=True)
    last = fields.Float(required=True, attribute="price")
    volume = fields.Float(required=True, attribute="volume_24h")
    high = fields.Float(required=True, attribute="highest_price_24h")
    low = fields.Float(required=True, attribute="lowest_price_24h")

    @pre_load
    def pre_load(self, data):
        data["source"] = s.BITSTAMP
        data["volume"] = float(data["volume"]) * float(data["last"])
        return data

    @post_load
    def post_load(self, data):
        super().post_load(data)
        return data
