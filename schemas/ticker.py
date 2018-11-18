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


class Ticker(Schema):
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
        open_time = data.get('openTime')
        if open_time:
            data['openTime'] = dateparser.parse(str(open_time)).isoformat()
        close_time = data.get('closeTime')
        if close_time:
            data['closeTime'] = dateparser.parse(str(close_time)).isoformat()
        return data

    @post_load
    def post_load(self, data):
        opened_on = data.get('opened_on')
        if opened_on:
            data['opened_on'] = opened_on.utcnow()
        closed_on = data.get('closed_on')
        if closed_on:
            data['closed_on'] = closed_on.utcnow()
        return data
