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
    current_app,
)
from flask_login import (
    login_required,
    current_user,
)


bp = Blueprint('transaction', __name__)


@bp.route('/transactions', methods=['GET'])
@login_required
def index():
    response = requests.get(
        url='{}transactions'.format(
            current_app.config['SERVER_API_BASE_URL']
        ),
        headers=dict(Authorization=current_user.id),
    )
    return dict(results=response.json()), response.status_code


@bp.route('/transaction/add', methods=['POST'])
@login_required
def add():
    response = requests.post(
        url='{}transaction/add'.format(
            current_app.config['SERVER_API_BASE_URL']
        ),
        headers=dict(Authorization=current_user.id),
        json=request.form.to_dict()
    )
    return response.json(), response.status_code
