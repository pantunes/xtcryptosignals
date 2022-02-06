__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import redis
import json
from marshmallow import (
    Schema,
    fields,
    post_dump,
)
from xtcryptosignals.common.utils import get_pairs_ex
from xtcryptosignals.tasks import settings as s
from xtcryptosignals.server.api.exchanges.binance.service import BinanceAPI


red = redis.Redis.from_url(s.BROKER_URL)
pairs = get_pairs_ex(s.SYMBOLS_PER_EXCHANGE)


class BalanceOutputSchema(Schema):
    coin_token = fields.String(required=True, attribute="asset")
    free = fields.Float(required=True)
    locked = fields.Float(required=True)

    @post_dump
    def post_dump(self, data):
        data["total"] = data["free"] + data["locked"]

        if data["coin_token"] != "USDT":
            key = s.REDIS_KEY_TICKER.format(
                source=s.BINANCE,
                symbol=f"{data['coin_token']}USDT",
                frequency=s.HISTORY_FREQUENCY[0],
            )
            ser_row = red.get(key)
            if ser_row:
                deser_row = json.loads(ser_row)
                price = float(deser_row["price"])
                data["price"] = price
        else:
            data["price"] = 1.0

        if "price" in data:
            # the ones configured in `settings_exchanges.py`
            data["total_price"] = data["total"] * data["price"]


class ExchangeBalanceOutputSchema(Schema):
    balances = fields.Nested(BalanceOutputSchema, many=True, required=True)

    @post_dump(pass_many=True)
    def post_dump(self, data, many):
        rows = []
        total = 0.0
        for x in data["balances"]:
            if x["free"] == 0 and x["locked"] == 0:
                continue
            if "price" in x:
                total += x["price"] * x["total"]
            rows.append(x)

        rows = sorted(
            rows, key=lambda i: i.get("total_price", 0.0), reverse=True
        )

        return dict(results=dict(rows=rows, total=total))


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
        data["total"] = data["price"] * data["amount"]

        try:
            token_pair = pairs[data["symbol"]]
        except KeyError:
            # Not supported - Must be added in project settings
            return

        data["coin_token"] = token_pair["token"]
        data["pair"] = token_pair["pair"]

        if data["type"] != "SELL":
            return

        if data["symbol"] not in self.symbols:
            rows = BinanceAPI(
                pkey=self.context["app"].config["SECRET_KEY"],
                auth=self.context["auth"],
            ).client.get_my_trades(symbol=data["symbol"], limit=200)
            rows.reverse()
            self.symbols.update({data["symbol"]: dict(rows=rows)})
        else:
            rows = self.symbols[data["symbol"]]["rows"]

        key = s.REDIS_KEY_TICKER.format(
            source=s.BINANCE,
            symbol=data["symbol"],
            frequency=s.HISTORY_FREQUENCY[0],
        )
        ser_row = red.get(key)
        if ser_row:
            deser_row = json.loads(ser_row)
            price = float(deser_row["price"])
            data["distance"] = ((data["price"] * 100) / price) - 100.0

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

        if "distance" in data and "position" in data:
            data["status"] = data["distance"] < data["position"]

    @post_dump(pass_many=True)
    def post_dump_pass_many(self, data, many):
        balance_potential = sum(
            [x["total"] for x in data if x["type"] == "SELL"]
        )
        return dict(results=data, balance_potential=balance_potential)


class ExchangeAccountStatusOutputSchema(Schema):
    success = fields.Boolean(required=True)
