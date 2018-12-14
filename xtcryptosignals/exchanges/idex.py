__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests


class Idex:
    def __init__(self):
        self.base_url = 'https://api.idex.market/returnTicker'

    def get_ticker(self, symbol):
        request = requests.post(
            self.base_url, json={'market': '_'.join(reversed(symbol))}
        )
        if request.status_code != 200:
            raise ValueError(
                'Error connecting IDEX on URL: {}'.format(self.base_url)
            )
        item = request.json()
        item.update(
            symbol=''.join(symbol)
        )
        return item
