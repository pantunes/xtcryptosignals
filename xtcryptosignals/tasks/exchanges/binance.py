__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from binance.client import Client as BinanceClient
from binance.exceptions import BinanceAPIException
from xtcryptosignals.tasks import settings as s


class Binance:
    def __init__(self):
        self.client = BinanceClient(s.BINANCE_API_KEY, s.BINANCE_API_SECRET)

    def get_ticker(self, symbol=None, pairs=None):
        ticker_kwargs = {}

        if symbol:
            ticker_kwargs = dict(symbol="".join(symbol))

        try:
            items_or_item = self.client.get_ticker(**ticker_kwargs)
        except (BinanceAPIException, Exception) as err:
            raise ValueError(str(err))

        if symbol:
            row = items_or_item
            row.update(ticker=symbol[0])
            return row

        rows = []
        _pairs = {x[0] + x[1]: x[0] for x in pairs}
        for row in items_or_item:
            if row["symbol"] in _pairs:
                row.update(ticker=_pairs[row["symbol"]])
                rows.append(row)
                if len(rows) >= len(_pairs):
                    break
        return rows
