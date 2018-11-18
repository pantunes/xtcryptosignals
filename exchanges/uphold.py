__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests
import settings as s


class Uphold:
    def __init__(self):
        self.base_url = 'https://api.uphold.com/v0/ticker/{}'

    def get_ticker(self, symbol):
        url = self.base_url.format(symbol)
        request = requests.get(url)
        if request.status_code != 200:
            raise ValueError(
                'Error connecting Uphold on URL: {}'.format(url)
            )
        item = request.json()
        item.update(
            symbol=symbol
        )
        return item
