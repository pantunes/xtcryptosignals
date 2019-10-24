__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests
from flask import Blueprint, Response, request
from flask_login import login_required, login_user, logout_user
from xtcryptosignals.client.api.auth.models import Auth
from xtcryptosignals.config import settings as s


bp = Blueprint('user', __name__)


@bp.route('/me', methods=['GET'])
@login_required
def me():
    return Response("/me")


@bp.route('/signup', methods=['POST'])
def signup():
    response = requests.post(
        url='{}signup'.format(s.SERVER_API_BASE_URL),
        json=dict(
            email=request.form.get('email'),
            password=request.form.get('password'),
        )
    )

    _json = response.json()

    if response.status_code == 200:
        login_user(Auth(_json))

    return _json, response.status_code


@bp.route('/login', methods=['POST'])
def login():
    response = requests.post(
        url='{}login'.format(s.SERVER_API_BASE_URL),
        json=dict(
            email=request.form.get('email'),
            password=request.form.get('password'),
        )
    )

    _json = response.json()

    if response.status_code == 200:
        login_user(Auth(_json))

    return _json, response.status_code


@bp.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return Response("/logout")
