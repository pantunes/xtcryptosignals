__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests


class Bilaxy:
    def __init__(self):
        self.base_url = 'https://www.bilaxy.com/api/v2/market/coins'

    def get_ticker(self, pairs):
        request = requests.get(self.base_url)
        if request.status_code != 200:
            raise ValueError(
                'Error connecting Bilaxy on URL: {}'.format(self.base_url)
            )
        response = request.json()['dataMap']
        _pairs = dict()
        for x, y in pairs:
            try:
                _pairs[y].append(x)
            except KeyError:
                _pairs[y] = [x]
        rows = list()
        url_template = 'https://api.bilaxy.com/v1/ticker?symbol={}'
        for x, y in _pairs.items():
            for z in response[x]:
                if z['fShortName'] in y:
                    url = url_template.format(z['fid'])
                    request = requests.get(url)
                    if request.status_code != 200:
                        raise ValueError(
                            'Error connecting Bilaxy on URL: {}'.format(url)
                        )
                    ticker = [z['fShortName'], x]
                    response_per_pair = request.json()['data']
                    response_per_pair.update(
                        symbol=''.join(ticker),
                        ticker=ticker[0]
                    )
                    rows.append(response_per_pair)
        return rows
