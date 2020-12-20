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
from xtcryptosignals.server.api.exchanges.binance.service import BinanceAPI


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
    symbols = dict()

    symbol = fields.String(required=True)
    price = fields.Float(required=True)
    amount = fields.Float(required=True, attribute="origQty")
    filled = fields.Float(required=True, attribute="executedQty")
    type = fields.String(required=True, attribute="side")
    created_on_ts = fields.Integer(required=True, attribute="time")

    @post_dump
    def post_dump_each(self, data):
        data["total"] = data["price"] + data["amount"]

        if data["type"] == "BUY":
            return

        if data["symbol"] not in self.symbols:
            rows = BinanceAPI(
                pkey=self.context["app"].config["SECRET_KEY"],
                auth=self.context["auth"],
            ).client.get_my_trades(symbol=data["symbol"], limit=40)
            rows.reverse()
            self.symbols.update({data["symbol"]: dict(rows=rows)})
        else:
            rows = self.symbols[data["symbol"]]["rows"]

        amount_total = 0.0
        total_total = 0.0

        for x in rows:
            if not x["isBuyer"]:
                continue
            if data["created_on_ts"] < x["time"]:
                continue

            qty = float(x["qty"])
            quote_qty = float(x["quoteQty"])

            amount_total += qty
            total_total += quote_qty

            if amount_total <= data["amount"]:
                continue

            amount_total -= qty
            total_total -= quote_qty

            ppc = quote_qty / qty
            rest = data["amount"] - amount_total

            amount_total += rest
            total_total += rest * ppc

            data["price_buy_average"] = total_total / amount_total
            data["position"] = (data["price"] * 100) / data[
                "price_buy_average"
            ] - 100
            break

    @post_dump(pass_many=True)
    def post_dump_pass_many(self, data, many):
        return dict(results=data)


class ExchangeAccountStatusOutputSchema(Schema):
    success = fields.Boolean(required=True)
