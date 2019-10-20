__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests


class Uphold:
    def __init__(self):
        self.base_url = 'https://api.uphold.com/v0/ticker/{}'

    def get_ticker(self, symbol):
        _symbol = ''.join(symbol)
        url = self.base_url.format(_symbol)
        request = requests.get(url)
        if request.status_code != 200:
            raise ValueError(
                'Error connecting Uphold on URL: {}'.format(url)
            )
        item = request.json()
        item.update(symbol=_symbol, ticker=symbol[0])
        return item
