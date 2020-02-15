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
        Crypto Fear & Greed Index + BTC data
        ---
        tags:
            - Charts
        security:
            - Bearer: []
        responses:
            200:
                description: Returns list of Crypto Fear & Greed Index \
                + BTC chart data format
        """
        return service.get_chart_fear_and_greed_index_and_btc(frequency)


class ChartCoinTokenFrequency(Resource):
    @validate_io()
    def get(self, coin_or_token, frequency):
        """
        Coin / Token chart data format
        ---
        tags:
            - Charts
        security:
            - Bearer: []
        responses:
            200:
                description: Returns list of Coin / Token chart data format
        """
        return service.get_chart_coin_or_token_frequency(
            coin_or_token, frequency
        )


api.add_resource(ChartFearAndGreedIndexAndBTC, "/charts/cfgi/BTC/<frequency>")
api.add_resource(ChartCoinTokenFrequency, "/charts/<coin_or_token>/<frequency>")
