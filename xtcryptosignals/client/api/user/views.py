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
    current_user,
)
from xtcryptosignals.client.api.auth.models import Auth


bp = Blueprint('user', __name__)


@bp.route('/info', methods=['GET'])
@login_required
def info():
    return Response('''<h5>Hey {name}! Welcome to XTCryptoSignals!</h5>
    This is an Open-source software platform that is in constant development.
    <br/><br/>
    For now you've been already able to create your user account but there are 
    no currently user features available.<br/><br/>
    Those are being developed and tested and once they are stable they will be 
    released.<br/><br/>
    Return back to check it out or stay tuned for the next releases 
    <a href="https://bitbucket.org/pantunes/xtcryptosignals">here</a>.'''.
                    format(**current_user.user))


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
