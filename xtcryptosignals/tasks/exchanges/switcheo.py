__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from switcheo.public_client import PublicClient


class Switcheo:
    def __init__(self):
        self.client = PublicClient(api_url='https://api.switcheo.network/')

    def get_ticker(self, pairs):
        _pairs = [x[0]+'_'+x[1] for x in pairs]
        _last_24h = self.client.get_last_24_hours()
        _last_prices = self.client.get_last_price()
        rows = list()
        for x in _last_24h:
            if x['pair'] not in _pairs:
                continue
            pos = x['pair'].find('_')
            x['price'] = _last_prices[x['pair'][:pos]][x['pair'][pos + 1:]]
            x['ticker'] = x['pair'].split('_')[0]
            rows.append(x)
            if len(rows) == len(pairs):
                break
        return rows
