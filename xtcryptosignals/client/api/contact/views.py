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
    request,
    Blueprint,
    current_app,
    session,
)


bp = Blueprint("contact", __name__)


@bp.route("/contact", methods=["POST"])
def contact():
    form_data = request.form

    try:
        if form_data["captcha"] != session["captcha"]:
            return dict(error="Bad Captcha."), 404
    except KeyError:
        return dict(error="Bad Captcha."), 404

    response = requests.post(
        url="{}contact".format(current_app.config["SERVER_API_BASE_URL"]),
        data=form_data,
    )
    return response.text, response.status_code
