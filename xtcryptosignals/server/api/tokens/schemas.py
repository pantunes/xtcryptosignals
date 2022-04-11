__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from marshmallow import Schema, fields


class TickerOutputSchema(Schema):
    symbol = fields.String(required=True)
    source = fields.String(required=True)
    ticker = fields.String(required=True)
    price = fields.Float(required=True)
    price_usdt = fields.Float(required=True)
    created_on = fields.String(required=True)
