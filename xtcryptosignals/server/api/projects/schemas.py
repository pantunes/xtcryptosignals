__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from millify import millify
from marshmallow import fields, post_dump
from xtcryptosignals.server.api.common.schemas import OutputSchema


class ProjectsOutputSchema(OutputSchema):
    name = fields.String(required=True)
    coin_or_token = fields.String(required=True)
    summary = fields.String(allow_none=True)
    website = fields.String(required=True)
    twitter = fields.String(required=True)
    wikipedia = fields.String(allow_none=True)


class ProjectTwitterOutputSchema(OutputSchema):
    num_followers = fields.String(allow_none=True)

    @post_dump
    def post_dump(self, data):
        if data["num_followers"]:
            data["num_followers"] = millify(data["num_followers"], precision=2)
        return data
