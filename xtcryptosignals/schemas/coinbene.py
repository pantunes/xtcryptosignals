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
)
import xtcryptosignals.settings as s


class Coinbene(Schema):
    symbol = fields.Str(required=True)
    source = fields.Str(required=True)
    last = fields.Float(required=True, attribute='price')
    vol = fields.Float(required=True, attribute='volume_24h')
    high = fields.Float(required=True, attribute='highest_price_24h')
    low = fields.Float(required=True, attribute='lowest_price_24h')

    @pre_load
    def pre_load(self, data):
        data['source'] = s.COINBENE
        data['high'] = data['24hrHigh']
        data['low'] = data['24hrLow']
        data['vol'] = float(data['24hrVol']) * float(data['last'])
        return data
