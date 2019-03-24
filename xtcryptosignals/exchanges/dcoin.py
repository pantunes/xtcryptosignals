__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests


class Dcoin:
    def __init__(self):
        self.base_url = 'https://openapi.dcoin.com/api/v1/allticker'

    def get_ticker(self, pairs):
        request = requests.get(self.base_url)
        if request.status_code != 200:
            raise ValueError(
                'Error connecting Dcoin on URL: {}'.format(self.base_url)
            )
        response = request.json()
        _pairs = ['_'.join(x).lower() for x in pairs]
        counter = 0
        rows = list()
        for x in response['ticker']:
            if counter == len(_pairs):
                break
            if x['symbol'] in _pairs:
                rows.append(x)
                counter += 1
        return rows
