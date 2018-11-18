__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = []
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from marshmallow import (
    Schema,
    fields,
    pre_load,
)
import settings as s


class Uphold(Schema):
    symbol = fields.Str(required=True)
    source = fields.Str(required=True)
    ask = fields.Float(required=True, attribute='price')

    @pre_load
    def pre_load(self, data):
        data['source'] = s.UPHOLD
