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
    request,
    session,
    current_app,
)
from flask_login import (
    login_required,
    login_user,
    logout_user,
    current_user,
)
from xtcryptosignals.client import login_manager
from xtcryptosignals.client.api.auth.models import Auth


bp = Blueprint("auth", __name__)


@login_manager.user_loader
def load_user(token):
    response = requests.get(
        url=f"{current_app.config['SERVER_API_BASE_URL']}auth",
        headers=dict(Authorization=token),
    )

    if response.status_code != 200:
        return

    _json = response.json()
    return Auth(_json)


@bp.route("/login", methods=["POST"])
def login():
    form_data = request.form.to_dict()

    try:
        if form_data["captcha"] != session["captcha"]:
            return dict(error="Bad credentials."), 404
    except KeyError:
        return dict(error="Bad credentials."), 404

    response = requests.post(
        url=f"{current_app.config['SERVER_API_BASE_URL']}login",
        json=form_data,
    )

    _json = response.json()

    if response.status_code == 200:
        login_user(Auth(_json))

    return _json, response.status_code


@bp.route("/logout", methods=["GET"])
@login_required
def logout():
    response = requests.post(
        url=f"{current_app.config['SERVER_API_BASE_URL']}logout",
        headers=dict(Authorization=current_user.id),
    )

    if response.status_code == 200:
        logout_user()
        session.clear()

    return {}, response.status_code


@bp.route("/subscription", methods=["POST"])
@login_required
def subscription():
    response = requests.post(
        url=f"{current_app.config['SERVER_API_BASE_URL']}subscription",
        headers=dict(Authorization=current_user.id),
        json=request.get_json(),
    )
    return {}, response.status_code


@bp.route("/favourites/<coin_or_token>", methods=["GET"])
def favourite_get(coin_or_token):
    if not current_user.is_authenticated:
        return {}, 401
    response = requests.get(
        url=f"{current_app.config['SERVER_API_BASE_URL']}favourites/{coin_or_token}",
        headers=dict(Authorization=current_user.id),
    )
    return response.json(), response.status_code


@bp.route("/favourites/<coin_or_token>", methods=["POST"])
def favourite_toggle(coin_or_token):
    if not current_user.is_authenticated:
        return {}, 401
    response = requests.post(
        url=f"{current_app.config['SERVER_API_BASE_URL']}favourites/{coin_or_token}",
        headers=dict(Authorization=current_user.id),
    )
    return response.json(), response.status_code
