__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from mongoengine import (
    StringField,
    URLField,
)
from xtcryptosignals.common.models import DocumentValidation


class Project(DocumentValidation):
    name = StringField(required=True, unique=True)
    summary = StringField()
    coin_or_token = StringField(required=True, unique=True)
    website = URLField(required=True)
    twitter = URLField(required=True)
    wikipedia = URLField()

    meta = {
        "collection": "project",
        "ordering": ["name"],
    }
