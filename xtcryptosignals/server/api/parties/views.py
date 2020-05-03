__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import redis
from flask import Blueprint
from flask_restful import Api, Resource
from xtcryptosignals.server.utils import validate_io
from xtcryptosignals.tasks import settings as s


bp = Blueprint("parties", __name__)
api = Api(bp)


red = redis.Redis.from_url(s.BROKER_URL)


class FearAndGreedIndex(Resource):
    @validate_io()
    def get(self):
        """
        Crypto Fear & Greed Index
        ---
        tags:
            - Parties
        security:
            - Bearer: []
        responses:
            200:
                description: Returns Crypto Fear & Greed Index
        """
        return dict(cfgi=int(red.get(s.REDIS_CFGI)))


api.add_resource(FearAndGreedIndex, "/parties/cfgi")
