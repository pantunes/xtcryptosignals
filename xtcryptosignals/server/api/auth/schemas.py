__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from marshmallow import Schema, fields
from xtcryptosignals.server.api.user.schemas import UserOutputSchema
from xtcryptosignals.server.api.common.schemas import OutputSchema


class AuthInputSchema(Schema):
    email = fields.String(required=True)
    password = fields.String(required=True)


class AuthSubscriptionInputSchema(Schema):
    endpoint = fields.URL(required=True)
    keys = fields.Dict(required=True)


class AuthOutputSchema(OutputSchema):
    user = fields.Nested(UserOutputSchema, required=True)
    token = fields.String(required=True)
