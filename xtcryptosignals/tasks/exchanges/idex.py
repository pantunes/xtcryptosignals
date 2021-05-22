__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"

try:
    from idex.client import Client
except ModuleNotFoundError:
    pass
from xtcryptosignals.tasks import settings as s


class Idex:
    def __init__(self):
        self.client = Client(s.IDEX_API_KEY, s.IDEX_ADDRESS, s.IDEX_PRIVATE_KEY)

    def get_ticker(self, symbol):
        item = self.client.get_ticker("_".join(reversed(symbol)))
        item.update(symbol="".join(symbol), ticker=symbol[0])
        return item
