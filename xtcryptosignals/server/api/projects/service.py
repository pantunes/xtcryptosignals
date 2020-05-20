__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from mongoengine import Q
from mongoengine.errors import ValidationError
from xtcryptosignals.server.api.projects.models import Project
from xtcryptosignals.tasks.models.project_twitter import ProjectTwitter


def projects():
    return Project.objects


def project_twitter(project):
    try:
        row = ProjectTwitter.objects(
            Q(project=project) & Q(num_followers__exists=True)
        ).first()
        if not row:
            raise ValueError("Project does not exist or no twitter data", 404)
    except ValidationError:
        raise ValueError("Invalid Project", 406)
    return row
