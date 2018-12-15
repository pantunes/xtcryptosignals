__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests
from requests.exceptions import SSLError


class Bithumb:
    def __init__(self):
        self.base_url = 'https://api.bithumb.com/public/ticker/{}'

    def get_ticker(self, symbol):
        url = self.base_url.format(symbol[0])
        try:
            request = requests.get(url)
        except SSLError:
            raise ValueError('SSLError in URL: {}'.format(url))
        if request.status_code != 200:
            raise ValueError(
                'Error connecting Bithumb on URL: {}'.format(url)
            )
        item = request.json()['data']
        item.update(
            symbol=''.join(symbol)
        )
        return item
