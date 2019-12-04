__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from flask import Blueprint
from flask_restful import Api, Resource
from xtcryptosignals.server.utils import (
    validate_io,
    user_auth,
)
from xtcryptosignals.server.api.auth import service
from xtcryptosignals.server.api.auth.schemas import (
    AuthInputSchema,
    AuthSubscriptionInputSchema,
    AuthOutputSchema,
)


bp = Blueprint('auth', __name__)
api = Api(bp)


class LoginPost(Resource):
    @validate_io(schema_in=AuthInputSchema, schema_out=AuthOutputSchema)
    def post(self, valid_data):
        """
        User authenticates
        ---
        tags:
            - Authentication
        parameters:
            - name: payload
              in: body
              example:
                {
                    email: 'some@email.com',
                    password: 'S0m3_p4ssw0rd',
                }
              required: true
        responses:
            200:
                description: User was logged in successfully
            400:
                description: Error in input validation
            401:
                description: Unauthorized
            402:
                description: Invalid JSON payload
            404:
                description: User not found
            412:
                description: Error when generating token
            415:
                description: Error in output pre-validation
            416:
                description: Error in output validation
        """
        return service.login(data=valid_data)


class LogoutPost(Resource):
    @validate_io()
    @user_auth()
    def post(self, auth):
        """
        User logs out
        ---
        tags:
            - Authentication
        security:
            - Bearer: []
        responses:
            200:
                description: User logged out successfully
            401:
                description: Unauthorized
        """
        service.logout(auth=auth)


class AuthGet(Resource):
    @validate_io(schema_out=AuthOutputSchema)
    @user_auth()
    def get(self, auth):
        """
        Checks if user session is valid
        ---
        tags:
            - Authentication
        security:
            - Bearer: []
        responses:
            200:
                description: User session is valid
            400:
                description: Error in session validation
            401:
                description: Unauthorized
        """
        return auth


class SubscriptionPost(Resource):
    @validate_io(schema_in=AuthSubscriptionInputSchema)
    @user_auth()
    def post(self, auth, valid_data):
        """
        Adds/Updates User's Subscription
        ---
        tags:
            - Authentication
        security:
            - Bearer: []
        responses:
            200:
                description: Subscription saved
            400:
                description: Error in input validation
            401:
                description: Unauthorized
        """
        service.subscription(auth=auth, data=valid_data)


api.add_resource(LoginPost, '/login')
api.add_resource(LogoutPost, '/logout')
api.add_resource(AuthGet, '/auth')
api.add_resource(SubscriptionPost, '/subscription')
