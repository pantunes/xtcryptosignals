__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from marshmallow import (
    fields,
    Schema,
    ValidationError,
    validates_schema,
)
from xtcryptosignals.server.api.common.schemas import OutputSchema


def _validate_name(n):
    if len(n.strip()) == 0:
        raise ValidationError('Must be filled in.')


def _validate_password(p):
    if not (8 <= len(p) <= 64):
        raise ValidationError('Length must be between 8 and 64 chars.')


class UserCreateInputSchema(Schema):
    name = fields.String(required=True, validate=_validate_name)
    email = fields.String(required=True)
    password = fields.String(required=True, validate=_validate_password)
    confirm_password = fields.String(required=True)

    @validates_schema
    def validate_confirm_password(self, data, **_):
        if data.get("password") != data.get("confirm_password"):
            raise ValidationError("Strings don't match (password).")


class UserOutputSchema(OutputSchema):
    name = fields.String(required=True)
    email = fields.String(required=True)
