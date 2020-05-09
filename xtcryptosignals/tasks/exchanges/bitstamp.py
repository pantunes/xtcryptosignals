__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests


class Bitstamp:
    def __init__(self):
        self.base_url = "https://www.bitstamp.net/api/v2/ticker/{}"

    def get_ticker(self, symbol):
        _symbol = "".join(symbol).lower()
        url = self.base_url.format(_symbol)
        request = requests.get(url)
        if request.status_code != 200:
            raise ValueError("Error connecting Bitstamp on URL: {}".format(url))
        item = request.json()
        item.update(symbol="".join(symbol), ticker=symbol[0])
        return item
