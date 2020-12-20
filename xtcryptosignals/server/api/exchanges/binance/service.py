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
from xtcryptosignals.server.api.exchanges.service import ExchangeAPI
from xtcryptosignals.server.crypto import Crypto


class BinanceAPI(ExchangeAPI):
    def __init__(self, pkey, auth):
        fkey = Crypto._get_fkey(key=pkey, salt=auth.user.salt)

        try:
            binance_secrets = auth.user.metadata["exchanges"]["binance"]
        except (KeyError, AttributeError):
            raise ValueError("No Binance(1).", 403)

        key = Crypto.decrypt(fkey, binance_secrets["api_key"])
        secret = Crypto.decrypt(fkey, binance_secrets["api_secret"])

        try:
            self.client = BinanceClient(key, secret)
        except BinanceAPIException:
            raise ValueError("No Binance(2).", 403)

    def get_balance(self):
        return self.client.get_account()

    def get_open_orders(self):
        return self.client.get_open_orders()

    def get_account_status(self):
        return self.client.get_account_status()
