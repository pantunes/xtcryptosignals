__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests


class BinanceDex:
    def __init__(self):
        self.base_url = 'https://dex.binance.org/api/v1/ticker/24hr'

    def get_ticker(self, pairs):
        request = requests.get(self.base_url)
        if request.status_code != 200:
            raise ValueError(
                'Error connecting Binance-Dex on URL: {}'.format(self.base_url)
            )
        response = request.json()

        _pairs = {
            x['symbol'][:x['symbol'].find('-')] +
            x['symbol'][x['symbol'].find('_')+1:]: x for x in response
        }

        rows = list()
        for x in pairs:
            symbol = ''.join(x)
            item = _pairs[symbol]
            item['symbol'] = symbol
            rows.append(item)

        return rows
