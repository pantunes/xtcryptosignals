__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests


class Bitmax:
    def __init__(self):
        self.base_url = 'https://bitmax.io/api/v1/ticker/24hr'

    def get_ticker(self, pairs):
        request = requests.get(self.base_url)
        if request.status_code != 200:
            raise ValueError(
                'Error connecting Bitmax on URL: {}'.format(self.base_url)
            )
        response = request.json()
        _pairs = ['/'.join(x) for x in pairs]
        counter = 0
        rows = list()
        for x in response:
            if counter == len(_pairs):
                break
            if x['symbol'] in _pairs:
                x.update(ticker=x['symbol'].split('/')[0])
                rows.append(x)
                counter += 1
        return rows
