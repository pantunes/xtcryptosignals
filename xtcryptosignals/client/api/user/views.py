__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests
from flask import (
    Blueprint,
    Response,
    request,
    current_app,
)
from flask_login import (
    login_required,
    login_user,
)
from xtcryptosignals.client.api.auth.models import Auth


bp = Blueprint('user', __name__)


@bp.route('/me', methods=['GET'])
@login_required
def me():
    return Response("/me")


@bp.route('/signup', methods=['POST'])
def signup():
    response = requests.post(
        url='{}signup'.format(current_app.config['SERVER_API_BASE_URL']),
        json=request.form.to_dict()
    )

    _json = response.json()

    if response.status_code == 200:
        login_user(Auth(_json))

    return _json, response.status_code
