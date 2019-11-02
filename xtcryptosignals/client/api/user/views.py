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
from xtcryptosignals import settings as s
from xtcryptosignals.client.api.auth.models import Auth


bp = Blueprint('user', __name__)


@bp.route('/info', methods=['GET'])
@login_required
def info():
    return Response('''<h5>Hey {name}! Welcome to XTCryptoSignals!</h5>
    This is an Open-source software platform that is in continuous development.
    <br/><br/>
    For now you can access your <a href="/portfolio/{frequency}">portfolio</a> 
    page and manage your assets.
    <br/>
    <br/>
    In case you are curious about further feature releases have a look 
    <a href="https://bitbucket.org/pantunes/xtcryptosignals">here</a>.
    <br/><br/>
    We hope you like this platform experience and please drop us some 
    <a href="javascript:open_modal('#modal_contact');">lines</a> in case 
    of any question.
    <br/><br/>
    The XTCryptoSignals Team
    '''.format(frequency=s.HISTORY_FREQUENCY[0], **current_user.user))


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
