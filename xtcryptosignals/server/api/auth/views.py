__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from flask import Blueprint, current_app
from flask_restful import Api, Resource
from xtcryptosignals.server.utils import (
    validate_io,
    user_auth,
)
from xtcryptosignals.server.api.auth import service
from xtcryptosignals.server.api.auth.schemas import (
    AuthInputSchema,
    AuthSubscriptionInputSchema,
    AuthExchangeBinanceKeysInputSchema,
    AuthOutputSchema,
)


bp = Blueprint("auth", __name__)
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
            400:
                description: Error in session validation
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
                description: Error in session validation
            401:
                description: Unauthorized
        """
        service.subscription(auth=auth, data=valid_data)


class ExchangeBinanceKeysPost(Resource):
    @validate_io(schema_in=AuthExchangeBinanceKeysInputSchema)
    @user_auth()
    def post(self, auth, valid_data):
        """
        Adds User's Exchange Binance keys
        ---
        tags:
            - Authentication
        parameters:
            - name: payload
              in: body
              example:
                {
                    api_key: 'some_key',
                    api_secret: 'some_secret',
                }
              required: true
        security:
            - Bearer: []
        responses:
            200:
                description: Keys saved
            400:
                description: Error in session validation
            401:
                description: Unauthorized
        """
        service.exchange_binance_keys(
            auth=auth, data=valid_data, pkey=current_app.config["SECRET_KEY"]
        )


class UserTokenFavouritesGet(Resource):
    @validate_io()
    @user_auth()
    def get(self, auth, coin_or_token):
        """
        Get User favourite coin or token
        ---
        tags:
            - User
        security:
            - Bearer: []
        responses:
            200:
                description: Favourite Coin/Token saved
            204:
                description: Coin/Token not in favourites
            400:
                description: Error in session validation
            401:
                description: Unauthorized
            405:
                description: Coin/Token does not exist
        """
        service.get_user_coin_or_token_favourite(
            auth=auth, coin_or_token=coin_or_token
        )


class UserTokenFavouritesPost(Resource):
    @validate_io()
    @user_auth()
    def post(self, auth, coin_or_token):
        """
        Toggle User favourite coin or token
        ---
        tags:
            - User
        security:
            - Bearer: []
        responses:
            200:
                description: Set/Unset done successfully
            400:
                description: Error in session validation
            401:
                description: Unauthorized
            404:
                description: Coin/Token not found
            405:
                description: Coin/Token does not exist
        """
        return service.toggle_user_coin_or_token_favourite(
            auth=auth, coin_or_token=coin_or_token
        )


class UserTokenFavouritesListGet(Resource):
    @validate_io()
    @user_auth()
    def get(self, auth):
        """
        Get User's list of favourite coins or tokens
        ---
        tags:
            - User
        responses:
            200:
                description: Returns list successfully
        """
        return service.get_favourites(auth=auth)


api.add_resource(LoginPost, "/login")
api.add_resource(LogoutPost, "/logout")
api.add_resource(AuthGet, "/auth")
api.add_resource(SubscriptionPost, "/subscription")
api.add_resource(ExchangeBinanceKeysPost, "/exchanges/binance")
api.add_resource(UserTokenFavouritesGet, "/favourites/<coin_or_token>")
api.add_resource(UserTokenFavouritesPost, "/favourites/<coin_or_token>")
api.add_resource(UserTokenFavouritesListGet, "/favourites")
