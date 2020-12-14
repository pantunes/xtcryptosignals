__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from xtcryptosignals.server.api.exchanges.service import ExchangeAPI
from binance.client import Client as BinanceClient
from xtcryptosignals.tasks import settings as s


class BinanceAPI(ExchangeAPI):
    def __init__(self, auth):
        super(BinanceAPI, self).__init__()
        self.client = BinanceClient(s.BINANCE_API_KEY, s.BINANCE_API_SECRET)
        self.auth = auth

    def get_balance(self):
        return self.client.get_account()

    def get_open_orders(self):
        return self.client.get_open_orders()

    def get_account_status(self):
        return self.client.get_account_status()
