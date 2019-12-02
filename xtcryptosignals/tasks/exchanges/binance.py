__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from xtcryptosignals.tasks import settings as s
from binance.client import Client
from binance.exceptions import BinanceAPIException


class Binance:
    def __init__(self):
        self.client = Client(s.BINANCE_API_KEY, s.BINANCE_API_SECRET)

    def get_ticker(self, *_, **kwargs):
        symbol = kwargs.get('symbol')
        if symbol:
            ticker_kwargs = dict(symbol=''.join(symbol))
        else:
            ticker_kwargs = dict()

        try:
            items_or_item = self.client.get_ticker(**ticker_kwargs)
        except (BinanceAPIException, Exception) as err:
            raise ValueError(str(err))

        if symbol:
            item = items_or_item
            item.update(ticker=symbol[0])
            return item

        items = list()
        pairs = [x[0] + x[1] for x in kwargs['pairs']]
        for item in items_or_item:
            if item['symbol'] in pairs:
                item.update(ticker=item['symbol'])
                items.append(item)
                if len(items) >= len(pairs):
                    break
        return items
