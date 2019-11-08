__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from flask import Blueprint
from flask_restful import Api, Resource
from xtcryptosignals.server.utils import validate_io
from xtcryptosignals.server.api.user import service
from xtcryptosignals.server.api.user.schemas import (
    UserCreateInputSchema,
    UserOutputSchema,
)


bp = Blueprint('user', __name__)
api = Api(bp)


class SignUpPost(Resource):
    @validate_io(schema_in=UserCreateInputSchema, schema_out=UserOutputSchema)
    def post(self, valid_data):
        """
        User signup
        ---
        tags:
            - User
        parameters:
            - name: payload
              in: body
              example:
                {
                    name: 'John Doe',
                    email: 'some@email.com',
                    password: 'S0m3_p4ssw0rd',
                    confirm_password: "S0m3_p4ssw0rd"
                }
              required: true
        responses:
            201:
                description: User account was created
            400:
                description: Error in input validation
            402:
                description: Invalid JSON payload
            406:
                description: E-mail address is invalid
            409:
                description: User account e-mail address already exists
        """
        return service.create_user(data=valid_data), 201


api.add_resource(SignUpPost, '/signup')
