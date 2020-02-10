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
from xtcryptosignals.server.api.charts import service
from xtcryptosignals.tasks import settings as s


bp = Blueprint("charts", __name__)
api = Api(bp)


red = redis.Redis.from_url(s.BROKER_URL)


class ChartFearAndGreedIndexAndBTC(Resource):
    @validate_io()
    def get(self, frequency):
        """
        Returns Crypto Fear & Greed Index + BTC data
        ---
        tags:
            - Charts
        security:
            - Bearer: []
        responses:
            200:
                description: Returns Crypto Fear & Greed Index + BTC data
        """
        return service.get_chart_fear_and_greed_index_and_btc(frequency)


api.add_resource(ChartFearAndGreedIndexAndBTC, "/charts/cfgi/btc/<frequency>")
