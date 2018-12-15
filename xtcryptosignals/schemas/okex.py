__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from marshmallow import (
    Schema,
    fields,
    pre_load,
    post_load
)
import xtcryptosignals.settings as s


class Okex(Schema):
    product_id = fields.Str(required=True, attribute='symbol')
    source = fields.Str(required=True)
    last = fields.Float(required=True, attribute='price')
    base_volume_24h = fields.Float(required=True, attribute='volume_24h')
    high_24h = fields.Float(required=True, attribute='highest_price_24h')
    low_24h = fields.Float(required=True, attribute='lowest_price_24h')

    @pre_load
    def pre_load(self, data):
        data['source'] = s.OKEX
        return data

    @post_load
    def post_load(self, data):
        data['symbol'] = data['symbol'].replace('-', '')
        return data
