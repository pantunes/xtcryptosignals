__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from marshmallow import (
    Schema,
    fields,
    pre_load,
)
import xtcryptosignals.settings as s


class Uphold(Schema):
    symbol = fields.Str(required=True)
    source = fields.Str(required=True)
    ask = fields.Float(required=True, attribute='price')

    @pre_load
    def pre_load(self, data):
        data['source'] = s.UPHOLD
        return data
