__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from marshmallow import Schema, fields


class ContactInputSchema(Schema):
    email = fields.String(required=True)
    reason = fields.String(required=True)
    message = fields.String(required=True)
