__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


class ExchangeAPI(object):
    def get_balance(self):
        raise NotImplementedError

    def get_open_orders(self):
        raise NotImplementedError

    def ping(self):
        raise NotImplementedError
