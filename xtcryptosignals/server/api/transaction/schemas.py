__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from marshmallow import (
    Schema,
    fields,
)
from xtcryptosignals.server.api.common.schemas import OutputSchema


class TransactionInputSchema(Schema):
    coin_token = fields.String(required=True)
    units = fields.Float(required=True)
    amount = fields.Float(required=True)
    added_on = fields.Date(required=True)
    in_or_out = fields.String(required=True)


class TransactionOutputSchema(OutputSchema):
    coin_token = fields.String(required=True)
    units = fields.Float(required=True)
    amount = fields.Float(required=True)
    unit_price = fields.Float(required=True)
    added_on = fields.Date(required=True)
    in_or_out = fields.String(required=True)
