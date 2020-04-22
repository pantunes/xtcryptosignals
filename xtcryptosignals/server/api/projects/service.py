__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from mongoengine.errors import (
    ValidationError,
    DoesNotExist,
)
from xtcryptosignals.server.api.projects.models import Project
from xtcryptosignals.tasks.models.project_twitter import ProjectTwitter


def projects():
    return Project.objects


def project_twitter(project):
    try:
        return ProjectTwitter.objects.get(project=project)
    except ValidationError:
        raise ValueError("Invalid Project", 406)
    except DoesNotExist:
        raise ValueError("Project does not exist", 404)
