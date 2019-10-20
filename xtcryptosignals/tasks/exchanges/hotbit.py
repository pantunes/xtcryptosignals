__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests


class Hotbit:
    def __init__(self):
        self.base_url = 'https://api.hotbit.io/api/v1/market.status24h'

    def get_ticker(self, pairs):
        request = requests.get(self.base_url)
        if request.status_code != 200:
            raise ValueError(
                'Error connecting Hotbit on URL: {}'.format(self.base_url)
            )
        response = request.json()
        rows = list()
        for x in pairs:
            _symbol = ''.join(x)
            item = response[_symbol]
            item.update(symbol=_symbol, ticker=x[0])
            rows.append(item)
        return rows
