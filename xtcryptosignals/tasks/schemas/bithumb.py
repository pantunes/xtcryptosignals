__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
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


class Bithumb(BaseSchema):
    symbol = fields.Str(required=True)
    source = fields.Str(required=True)
    buy_price = fields.Float(required=True, attribute='price')
    fluctate_rate_1d = fields.Float(
        required=True, attribute='price_change_24h'
    )
    volume_1day = fields.Float(required=True, attribute='volume_24h')
    units_traded = fields.Int(required=True, attribute='number_trades_24h')
    max_price = fields.Float(required=True, attribute='highest_price_24h')
    min_price = fields.Float(required=True, attribute='lowest_price_24h')

    @pre_load
    def pre_load(self, data):
        data['source'] = s.BITHUMB
        data['units_traded'] = int(round(float(data['units_traded']), 0))
        data['fluctate_rate_1d'] = data['24H_fluctate_rate']
        return data

    @post_load
    def post_load(self, data):
        super().post_load(data)
        return data
