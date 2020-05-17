__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from kucoin.client import Client
from kucoin.exceptions import KucoinAPIException
from xtcryptosignals.tasks import settings as s


class Kucoin:
    def __init__(self):
        self.client = Client(
            s.KUCOIN_API_KEY, s.KUCOIN_API_SECRET, s.KUCOIN_API_PASSPHRASE
        )

    def get_ticker(self, symbol):
        _symbol = "-".join(symbol)

        try:
            item = self.client.get_ticker(_symbol)
        except (KucoinAPIException, Exception) as err:
            raise ValueError(str(err))

        try:
            item.update(self.client.get_24hr_stats(_symbol))
        except (KucoinAPIException, Exception) as err:
            raise ValueError(str(err))

        item.update(ticker=symbol[0])
        return item
