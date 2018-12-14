__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests


class Bibox:
    def __init__(self):
        self.base_url = 'https://api.bibox.com/v1/mdata?cmd=ticker&pair={}'

    def get_ticker(self, symbol):
        _symbol = '_'.join(symbol)
        url = self.base_url.format(_symbol)
        request = requests.get(url)
        if request.status_code != 200:
            raise ValueError(
                'Error connecting Bibox on URL: {}'.format(url)
            )
        return request.json()['result']
