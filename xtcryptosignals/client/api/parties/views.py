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


bp = Blueprint("parties", __name__)


@bp.route("/parties/cfgi", methods=["GET"])
def cfgi():
    response = requests.get(
        url="{}parties/cfgi".format(current_app.config["SERVER_API_BASE_URL"]),
    )
    return response.json(), response.status_code
