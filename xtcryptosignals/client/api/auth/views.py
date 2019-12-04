__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests
from flask import (
    Blueprint,
    request,
)
from flask_login import (
    login_required,
    login_user,
    logout_user,
    current_user,
)
from flask import session, current_app
from xtcryptosignals.client import login_manager
from xtcryptosignals.client.api.auth.models import Auth


bp = Blueprint('auth', __name__)


@login_manager.user_loader
def load_user(token):
    response = requests.get(
        url='{}auth'.format(current_app.config['SERVER_API_BASE_URL']),
        headers=dict(Authorization=token),
    )

    if response.status_code != 200:
        return

    _json = response.json()
    return Auth(_json)


@bp.route('/login', methods=['POST'])
def login():
    response = requests.post(
        url='{}login'.format(current_app.config['SERVER_API_BASE_URL']),
        json=request.form.to_dict()
    )

    _json = response.json()

    if response.status_code == 200:
        login_user(Auth(_json))

    return _json, response.status_code


@bp.route('/logout', methods=['GET'])
@login_required
def logout():
    response = requests.post(
        url='{}logout'.format(current_app.config['SERVER_API_BASE_URL']),
        headers=dict(Authorization=current_user.id)
    )

    if response.status_code == 200:
        logout_user()
        session.clear()

    return {}, response.status_code


@bp.route('/subscription', methods=['POST'])
@login_required
def subscription():
    response = requests.post(
        url='{}subscription'.format(current_app.config['SERVER_API_BASE_URL']),
        headers=dict(Authorization=current_user.id),
        json=request.get_json()
    )
    return {}, response.status_code
