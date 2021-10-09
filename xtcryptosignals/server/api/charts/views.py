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
        Crypto Fear & Greed Index + Coin/Token data
        ---
        tags:
            - Charts
        security:
            - Bearer: []
        parameters:
            - name: frequency
              in: path
              required: true
        responses:
            200:
                description: Returns list of Crypto Fear & Greed Index \
                + BTC chart data format
            400:
                description: Error in input validation
        """
        if frequency not in (
            "1d",
            "1w",
            "4w",
        ):
            return dict(error="Frequency is incorrect."), 400

        return service.get_chart_fear_and_greed_index(
            coin_or_token="BTC",
            frequency=frequency,
        )


class ChartCoinTokenFrequency(Resource):
    @validate_io()
    def get(self, coin_or_token, frequency):
        """
        Coin/Token chart data format
        ---
        tags:
            - Charts
        security:
            - Bearer: []
        parameters:
            - name: coin_or_token
              in: path
              required: true
            - name: frequency
              in: path
              required: true
        responses:
            200:
                description: Returns list of Coin / Token chart data format
            400:
                description: Error in input validation
        """
        return service.get_chart_coin_or_token_frequency(
            coin_or_token=coin_or_token,
            frequency=frequency,
        )


class ChartTetherBTC(Resource):
    @validate_io()
    def get(self, frequency):
        """
        Tether + Coin/Token chart data format
        ---
        tags:
            - Charts
        security:
            - Bearer: []
        parameters:
            - name: frequency
              in: path
              required: true
        responses:
            200:
                description: Returns list Tether + BTC chart data format
            400:
                description: Error in input validation
        """
        if frequency not in (
            "1h",
            "1d",
            "1w",
            "4w",
        ):
            return dict(error="Frequency is incorrect."), 400

        return service.get_chart_tether_btc(
            coin_or_token="BTC",
            frequency=frequency,
        )


class ChartTwitter(Resource):
    @validate_io()
    def get(self, project, frequency):
        """
        Twitter chart data format
        ---
        tags:
            - Charts
        security:
            - Bearer: []
        parameters:
            - name: project
              in: path
              required: true
            - name: frequency
              in: path
              required: true
        responses:
            200:
                description: Returns list Twitter chart data format
            400:
                description: Error in input validation
            404:
                description: Project not found
            405:
                description: Project is invalid
        """
        if frequency not in ("1d",):
            return dict(error="Frequency is incorrect."), 400

        return service.get_chart_twitter(project=project, frequency=frequency)


api.add_resource(ChartFearAndGreedIndexAndBTC, "/charts/cfgi/BTC/<frequency>")
api.add_resource(ChartCoinTokenFrequency, "/charts/<coin_or_token>/<frequency>")
api.add_resource(ChartTetherBTC, "/charts/tether/BTC/<frequency>")
api.add_resource(ChartTwitter, "/charts/twitter/<project>/<frequency>")
