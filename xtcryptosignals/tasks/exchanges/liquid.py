__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests
from requests.exceptions import SSLError


class Liquid:
    def __init__(self):
        self.base_url = "https://api.liquid.com/products/{}"

    def get_ticker(self, symbol):
        _symbol = "".join(symbol)
        mapping = {"EWTBTC": 553, "EWTETH": 554}
        url = self.base_url.format(mapping[_symbol])
        try:
            request = requests.get(url)
        except SSLError:
            raise ValueError(f"SSLError in URL: {url}")
        if request.status_code != 200:
            raise ValueError(f"Error connecting Liquid on URL: {url}")
        item = request.json()
        item.update(symbol=_symbol, ticker=symbol[0])
        return item
