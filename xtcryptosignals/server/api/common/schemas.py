__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from marshmallow import fields, Schema


class OutputSchema(Schema):
    _id = fields.String(required=True, attribute='id')
    created_on = fields.DateTime(required=True)
    modified_on = fields.DateTime(allow_none=True)
