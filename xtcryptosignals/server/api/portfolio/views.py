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

from xtcryptosignals.server.api.portfolio import service
from xtcryptosignals.server.utils import (
    validate_io,
    user_auth,
)

bp = Blueprint("portfolio", __name__)
api = Api(bp)


class Portfolio(Resource):
    @validate_io()
    @user_auth()
    def get(self, auth):
        """
        User's Portfolio
        ---
        tags:
            - Portfolio
        security:
            - Bearer: []
        responses:
            200:
                description: Returns User's Portfolio
            400:
                description: Error in session validation
            401:
                description: Unauthorized
        """
        return service.portfolio(auth)


api.add_resource(Portfolio, "/portfolio")
