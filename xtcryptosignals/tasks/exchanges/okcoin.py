__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests


class Okcoin:
    def __init__(self):
        self.base_url = "https://www.okcoin.com/api/v5/market/ticker?instId={}-{}"

    def get_ticker(self, symbol):
        url = self.base_url.format(*symbol)
        request = requests.get(url)
        if request.status_code != 200:
            raise ValueError(f"Error connecting OkCoin on URL: {url}")
        item = request.json()["data"][0]
        item.update(symbol="".join(symbol), ticker=symbol[0])
        return item
