__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests
from flask import (
    Blueprint,
    current_app,
)


bp = Blueprint("charts", __name__)


@bp.route("/charts/cfgi/BTC/<frequency>", methods=["GET"])
def cfgi_btc(frequency):
    response = requests.get(
        url=f"{current_app.config['SERVER_API_BASE_URL']}charts/cfgi/BTC/{frequency}"
    )
    return response.json(), response.status_code


@bp.route("/charts/<coin_or_token>/<frequency>", methods=["GET"])
def coin_or_token_frequency(coin_or_token, frequency):
    response = requests.get(
        url=f"{current_app.config['SERVER_API_BASE_URL']}charts/{coin_or_token}/{frequency}"
    )
    return response.json(), response.status_code


@bp.route("/charts/tether/<coin_or_token>/<frequency>", methods=["GET"])
def tether(coin_or_token, frequency):
    response = requests.get(
        url=f"{current_app.config['SERVER_API_BASE_URL']}charts/tether/{coin_or_token}/{frequency}"
    )
    return response.json(), response.status_code


@bp.route("/charts/twitter/<project>/<frequency>", methods=["GET"])
def twitter(project, frequency):
    response = requests.get(
        url=f"{current_app.config['SERVER_API_BASE_URL']}charts/twitter/{project}/{frequency}"
    )
    return response.json(), response.status_code
