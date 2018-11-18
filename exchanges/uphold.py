__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = []
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests
import settings as s


class Uphold:
    def __init__(self):
        self.base_url = 'https://api.uphold.com/v0/ticker'

    def get_ticker(self, symbol):
        url = '{}/{}'.format(self.base_url, symbol)
        request = requests.get(url)
        if request.status_code != 200:
            raise ValueError('Error connecting Uphold on URL: {}'.format(url))
        item = request.json()
        item.update(
            source=s.UPHOLD,
            symbol=symbol,
            lastPrice=item['ask'],
        )
        return item
