__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests


class Coinbene:
    def __init__(self):
        self.base_url = 'https://api.coinbene.com/v1/market/ticker?symbol={}'

    def get_ticker(self, symbol):
        _symbol = ''.join(symbol)
        url = self.base_url.format(_symbol)
        request = requests.get(url)
        if request.status_code != 200:
            raise ValueError(
                'Error connecting Coinbene on URL: {}'.format(url)
            )
        item = request.json()['ticker'][0]
        item.update(ticker=symbol[0])
        return item
