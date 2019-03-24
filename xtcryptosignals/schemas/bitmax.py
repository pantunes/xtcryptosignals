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
    post_load,
)
import xtcryptosignals.settings as s


class Bitmax(Schema):
    symbol = fields.Str(required=True)
    source = fields.Str(required=True)
    closePrice = fields.Float(required=True, attribute='price')
    volume = fields.Float(required=True, attribute='volume_24h')
    highPrice = fields.Float(required=True, attribute='highest_price_24h')
    lowPrice = fields.Float(required=True, attribute='lowest_price_24h')

    @pre_load
    def pre_load(self, data):
        data['source'] = s.BITMAX
        return data

    @post_load
    def post_load(self, data):
        data['symbol'] = data['symbol'].replace('/', '')
        data['volume_24h'] = data['volume_24h'] * data['price']
        return data
