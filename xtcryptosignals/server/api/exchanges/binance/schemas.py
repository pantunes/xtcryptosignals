__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from marshmallow import (
    Schema,
    fields,
    post_dump,
)


class BalanceOutputSchema(Schema):
    coin_token = fields.String(required=True, attribute="asset")
    free = fields.Float(required=True)
    locked = fields.Float(required=True)

    @post_dump
    def post_dump(self, data):
        data["total"] = data["free"] + data["locked"]


class ExchangeBalanceOutputSchema(Schema):
    balances = fields.Nested(BalanceOutputSchema, many=True, required=True)

    @post_dump(pass_many=True)
    def post_dump(self, data, many):
        rows = []
        for x in data["balances"]:
            if x["free"] == 0 and x["locked"] == 0:
                continue
            rows.append(x)
        return dict(results=rows)


class ExchangeOpenOrdersOutputSchema(Schema):
    symbol = fields.String(required=True)
    price = fields.Float(required=True)
    amount = fields.Float(required=True, attribute="origQty")
    filled = fields.Float(required=True, attribute="executedQty")
    type = fields.String(required=True, attribute="side")

    @post_dump(pass_many=True)
    def post_dump(self, data, many):
        return dict(results=data)


class ExchangeAccountStatusOutputSchema(Schema):
    success = fields.Boolean(required=True)
