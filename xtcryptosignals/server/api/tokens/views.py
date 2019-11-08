__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from flask import Blueprint
from flask_restful import Api, Resource
from xtcryptosignals.server.utils import validate_io
from xtcryptosignals.tasks import settings as s


bp = Blueprint('tokens', __name__)
api = Api(bp)


class FrequencyGet(Resource):
    @validate_io()
    def get(self):
        """
        Gets configured History Frequency
        ---
        tags:
            - Tokens
        responses:
            200:
                description: Returns list successfully
        """
        return s.HISTORY_FREQUENCY, 200


class SymbolsGet(Resource):
    @validate_io()
    def get(self):
        """
        Gets configured Symbols per Exchange
        ---
        tags:
            - Tokens
        responses:
            200:
                description: Returns list successfully
        """
        return s.SYMBOLS_PER_EXCHANGE, 200


api.add_resource(FrequencyGet, '/tokens/frequency')
api.add_resource(SymbolsGet, '/tokens/symbols')
