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
from xtcryptosignals.server.utils import (
    validate_io,
    user_auth,
)
from xtcryptosignals.server.api.exchanges import service
from xtcryptosignals.tasks import settings as s


bp = Blueprint("exchange", __name__)
api = Api(bp)


class ExchangeBalance(Resource):
    @validate_io()
    @user_auth()
    def get(self, auth, exchange):
        """
        User's Exchange balance
        ---
        tags:
            - Exchange
        security:
            - Bearer: []
        responses:
            200:
                description: Returns User balance
            400:
                description: Error in session validation
            401:
                description: Unauthorized
        """
        if exchange not in (s.BINANCE,):
            return dict(error="Invalid Exchange."), 400
        return service.get_balance(auth, exchange=exchange)


class ExchangeOpenOrders(Resource):
    @validate_io()
    @user_auth()
    def get(self, auth, exchange):
        """
        User's Exchange open orders
        ---
        tags:
            - Exchange
        security:
            - Bearer: []
        responses:
            200:
                description: Returns User open orders
            400:
                description: Error in session validation
            401:
                description: Unauthorized
        """
        if exchange not in (s.BINANCE,):
            return dict(error="Invalid Exchange."), 400
        return service.get_open_orders(auth, exchange=exchange)


api.add_resource(ExchangeBalance, "/exchange/<exchange>/balance")
api.add_resource(ExchangeOpenOrders, "/exchange/<exchange>/open-orders")
