__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests


class CoinbasePro:
    def __init__(self):
        self.base_urls = (
            "https://api.pro.coinbase.com/products/{0}-{1}/stats",
            "https://api.pro.coinbase.com/products/{0}-{1}/ticker",
        )

    def get_ticker(self, symbol):
        item = {}

        for i in range(2):
            url = self.base_urls[i].format(*symbol)

            request = requests.get(url)
            if request.status_code != 200:
                raise ValueError(f"Error connecting CoinbasePro on URL: {url}")
            item.update(request.json())

        item.update(symbol="".join(symbol), ticker=symbol[0])
        return item
