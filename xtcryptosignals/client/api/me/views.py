__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from flask import Blueprint, Response
from flask_login import login_required, login_user
from xtcryptosignals.client.api.auth.models import User


bp = Blueprint('me', __name__)


@bp.route('/me', methods=['GET'])
@login_required
def me():
    return Response("/me")


@bp.route('/login', methods=['GET'])
def login():
    login_user(User(1234))
    return Response("/login")
