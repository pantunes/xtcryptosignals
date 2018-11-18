__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = []
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import dateparser
from marshmallow import (
    Schema,
    fields,
    pre_load,
    post_load
)
import settings as s


class Binance(Schema):
    symbol = fields.Str(required=True)
    source = fields.Str(required=True)
    openTime = fields.DateTime(attribute='opened_on')
    closeTime = fields.DateTime(attribute='closed_on')
    count = fields.Int(attribute='number_trades_24h')
    quoteVolume = fields.Float(attribute='volume_24h')
    priceChangePercent = fields.Float(attribute='price_change_24h_percent')
    lastPrice = fields.Float(required=True, attribute='price')
    highPrice = fields.Float(attribute='highest_price_24h')
    lowPrice = fields.Float(attribute='lowest_price_24h')

    @pre_load
    def pre_load(self, data):
        data['source'] = s.BINANCE
        data['openTime'] = dateparser.parse(str(data['openTime'])).isoformat()
        data['closeTime'] = dateparser.parse(str(data['closeTime'])).isoformat()
        return data

    @post_load
    def post_load(self, data):
        data['opened_on'] = data['opened_on'].utcnow()
        data['closed_on'] = data['closed_on'].utcnow()
        return data
