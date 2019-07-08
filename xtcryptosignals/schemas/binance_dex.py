__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from marshmallow import pre_load
import xtcryptosignals.settings as s
from xtcryptosignals.schemas.binance import Binance


class BinanceDex(Binance):
    pass

    @pre_load
    def pre_load(self, data):
        super(BinanceDex, self).pre_load(data)
        data['source'] = s.BINANCE_DEX
        return data
