__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from cryptography.fernet import InvalidToken
from binance.client import Client as BinanceClient
from binance.exceptions import BinanceAPIException, BinanceRequestException
from xtcryptosignals.server.api.exchanges.service import ExchangeAPI
from xtcryptosignals.server.crypto import Crypto


class BinanceAPI(ExchangeAPI):
    def __init__(self, pkey, auth):
        fkey = Crypto._get_fkey(key=pkey, salt=auth.user.salt)

        try:
            binance_secrets = auth.user.metadata["exchanges"]["binance"]
        except (KeyError, AttributeError):
            raise ValueError("No Binance(1).", 403)

        try:
            key = Crypto.decrypt(fkey, binance_secrets["api_key"])
            secret = Crypto.decrypt(fkey, binance_secrets["api_secret"])
        except InvalidToken:
            raise ValueError("No Binance(2).", 403)

        try:
            self.client = BinanceClient(key, secret)
        except BinanceAPIException:
            raise ValueError("No Binance(3).", 403)

    def get_balance(self):
        try:
            return self.client.get_account()
        except BinanceAPIException:
            raise ValueError("No Binance(4).", 403)

    def get_open_orders(self):
        try:
            return self.client.get_open_orders()
        except BinanceAPIException:
            raise ValueError("No Binance(5).", 403)

    def ping(self):
        try:
            return {"success": self.client.ping() == {}}
        except BinanceRequestException:
            raise ValueError("No Binance(6).", 403)
        except BinanceAPIException:
            raise ValueError("No Binance(7).", 403)
