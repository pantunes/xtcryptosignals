__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from marshmallow import fields, Schema, ValidationError
from xtcryptosignals.server.api.common.schemas import OutputSchema


def _validate_password(p):
    if not (8 <= len(p) <= 64):
        raise ValidationError('Length must be between 8 and 64 chars.')


class UserCreateInputSchema(Schema):
    email = fields.String(required=True)
    password = fields.String(required=True, validate=_validate_password)


class UserOutputSchema(OutputSchema):
    email = fields.String(required=True)
