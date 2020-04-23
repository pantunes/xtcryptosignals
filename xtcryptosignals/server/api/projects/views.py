__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from flask import Blueprint
from flask_restful import Api, Resource
from xtcryptosignals.server.utils import validate_io
from xtcryptosignals.server.api.projects import service
from xtcryptosignals.server.api.projects.schemas import (
    ProjectsOutputSchema,
    ProjectTwitterOutputSchema,
)


bp = Blueprint("projects", __name__)
api = Api(bp)


class Projects(Resource):
    @validate_io(schema_out=ProjectsOutputSchema, many_out=True)
    def get(self):
        """
        Gets Projects
        ---
        tags:
            - Projects
        security:
            - Bearer: []
        responses:
            200:
                description: Returns Projects
        """
        return service.projects()


class ProjectTwitter(Resource):
    @validate_io(schema_out=ProjectTwitterOutputSchema)
    def get(self, project):
        """
        Gets Project's Twitter data
        ---
        tags:
            - Projects
        security:
            - Bearer: []
        parameters:
            - name: project
              in: path
              required: true
        responses:
            200:
                description: Returns Project's Twitter data
            404:
                description: Project not found
            406:
                description: Invalid Project
        """
        return service.project_twitter(project=project)


api.add_resource(Projects, "/projects")
api.add_resource(ProjectTwitter, "/projects/twitter/<project>")
