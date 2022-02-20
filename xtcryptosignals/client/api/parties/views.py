__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import random
import string
import requests
from flask import (
    Blueprint,
    current_app,
    session,
)
import base64
from captcha.image import ImageCaptcha


bp = Blueprint("parties", __name__)


@bp.route("/parties/cfgi", methods=["GET"])
def cfgi():
    response = requests.get(
        url=f"{current_app.config['SERVER_API_BASE_URL']}parties/cfgi",
    )
    return response.json(), response.status_code


@bp.route("/parties/captcha", methods=["GET"])
def captcha():
    val = "".join(
        [
            random.choice(string.ascii_lowercase + string.digits)
            for _ in range(6)
        ]
    )

    image = ImageCaptcha()
    _captcha = image.generate(val)

    session["captcha"] = val

    return dict(captcha=base64.b64encode(_captcha.getvalue()).decode()), 201
