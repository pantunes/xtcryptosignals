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
from xtcryptosignals.tasks.schemas.base import BaseSchema
from xtcryptosignals.tasks import settings as s


class Liquid(BaseSchema):
    symbol = fields.Str(required=True)
    source = fields.Str(required=True)
    last_traded_price = fields.Float(required=True, attribute="price")
    last_price_24h = fields.Float(required=True, attribute="price_change_24h")
    volume_24h = fields.Float(required=True)

    @pre_load
    def pre_load(self, data):
        data["source"] = s.LIQUID
        data["volume_24h"] = float(data["volume_24h"]) * float(
            data["last_traded_price"]
        )
        return data

    @post_load
    def post_load(self, data):
        super().post_load(data)
        return data
