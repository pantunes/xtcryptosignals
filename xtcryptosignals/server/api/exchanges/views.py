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
from xtcryptosignals.tasks import settings as s
from xtcryptosignals.server.api.exchanges.binance.service import BinanceAPI
from xtcryptosignals.server.api.exchanges.binance.schemas import (
    ExchangeBalanceOutputSchema,
    ExchangeOpenOrdersOutputSchema,
    ExchangeAccountStatusOutputSchema,
)


bp = Blueprint("exchange", __name__)
api = Api(bp)


EXCHANGE_APIS = {
    s.BINANCE: BinanceAPI,
    # ...
}


class ExchangeBalance(Resource):
    @validate_io(
        schema_out=ExchangeBalanceOutputSchema, skip_validate=True,
    )
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

        exchange_api = EXCHANGE_APIS[exchange](auth=auth)
        return exchange_api.get_balance()


class ExchangeOpenOrders(Resource):
    @validate_io(
        schema_out=ExchangeOpenOrdersOutputSchema,
        many_out=True,
        skip_validate=True,
    )
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

        exchange_api = EXCHANGE_APIS[exchange](auth=auth)
        return exchange_api.get_open_orders()


class ExchangeAccountStatus(Resource):
    @validate_io(schema_out=ExchangeAccountStatusOutputSchema)
    @user_auth()
    def get(self, auth, exchange):
        """
        User's Exchange account status
        ---
        tags:
            - Exchange
        security:
            - Bearer: []
        responses:
            200:
                description: Returns User account status
            400:
                description: Error in session validation
            401:
                description: Unauthorized
        """
        if exchange not in (s.BINANCE,):
            return dict(error="Invalid Exchange."), 400

        exchange_api = EXCHANGE_APIS[exchange](auth=auth)
        return exchange_api.get_account_status()


api.add_resource(ExchangeAccountStatus, "/exchange/<exchange>/account/status")
api.add_resource(ExchangeBalance, "/exchange/<exchange>/balance")
api.add_resource(ExchangeOpenOrders, "/exchange/<exchange>/orders/open")
