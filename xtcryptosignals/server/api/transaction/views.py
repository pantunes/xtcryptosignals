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
from xtcryptosignals.server.api.transaction import service
from xtcryptosignals.server.api.transaction.schemas import (
    TransactionInputSchema,
    TransactionOutputSchema,
)


bp = Blueprint('transaction', __name__)
api = Api(bp)


class TransactionAdd(Resource):
    @validate_io(schema_in=TransactionInputSchema)
    @user_auth()
    def post(self, auth, valid_data):
        """
        Adds Transaction
        ---
        tags:
            - Transactions
        security:
            - Bearer: []
        parameters:
            - name: payload
              in: body
              example:
                {
                    coin_token: 'BTC',
                    units: 0.0234,
                    amount: 450,
                    added_on: 08/10/2019,
                    in_or_out: 'in',
                }
              required: true
        responses:
            201:
                description: Added transaction successfully
            400:
                description: Error in input validation
            401:
                description: Unauthorized
            402:
                description: Invalid JSON payload
        """
        return service.add_transaction(auth, data=valid_data), 201


class Transactions(Resource):
    @validate_io(schema_out=TransactionOutputSchema, many_out=True)
    @user_auth()
    def get(self, auth):
        """
        Returns a list of the User's Transactions
        ---
        tags:
            - Transactions
        security:
            - Bearer: []
        responses:
            200:
                description: Returns List of Transactions
            400:
                description: Error in session validation
            401:
                description: Unauthorized
        """
        return service.transactions(auth), 200


api.add_resource(TransactionAdd, '/transaction/add')
api.add_resource(Transactions, '/transactions')
