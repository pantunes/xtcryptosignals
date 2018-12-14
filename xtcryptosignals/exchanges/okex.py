__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests


class Okex:
    def __init__(self):
        self.base_url = 'https://www.okex.com/api/spot/v3/' \
                        'instruments/{}/ticker'

    def get_ticker(self, symbol):
        _symbol = '-'.join(symbol)
        url = self.base_url.format(_symbol)
        request = requests.get(url)
        if request.status_code != 200:
            raise ValueError(
                'Error connecting OKEx on URL: {}'.format(url)
            )
        return request.json()
