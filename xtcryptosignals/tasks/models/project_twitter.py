__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from mongoengine import (
    LongField,
    DateField,
    ReferenceField,
)
from xtcryptosignals.common.models import DocumentValidation
from xtcryptosignals.server.api.projects.models import Project


class ProjectTwitter(DocumentValidation):
    num_followers = LongField()
    project = ReferenceField(Project, required=True)
    added_on = DateField(required=True)

    meta = {
        "collection": "project_twitter",
        "indexes": [
            {
                "fields": (
                    "project",
                    "added_on",
                ),
                "unique": True,
            }
        ],
        "ordering": ["-added_on"],
    }
