__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from marshmallow import (
    fields,
    pre_load,
    post_load,
)
from xtcryptosignals.tasks.schemas.base import BaseSchema
from xtcryptosignals.tasks import settings as s


class Uphold(BaseSchema):
    symbol = fields.Str(required=True)
    ticker = fields.Str(required=True)
    source = fields.Str(required=True)
    ask = fields.Float(required=True, attribute='price')

    @pre_load
    def pre_load(self, data):
        data['source'] = s.UPHOLD
        return data

    @post_load
    def post_load(self, data):
        super().post_load(data)
        return data
