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
    Response,
    request,
    current_app,
    session,
    escape,
    g,
)
from flask_login import (
    login_required,
    login_user,
    current_user,
)
from xtcryptosignals.client import service
from xtcryptosignals.client.api.auth.models import Auth


bp = Blueprint("user", __name__)


@bp.before_request
def before_request():
    g.HISTORY_FREQUENCY, _ = service.get_history_frequency()


@bp.route("/info", methods=["GET"])
@login_required
def info():
    return Response(
        f"""<h5>Welcome to <code>XTCryptoSignals</code>!</h5>
    Hi {escape(current_user.user["name"])},
    <br/><br/>
    This is an open-source software platform that is in 
    continuous development.
    <br/><br/>
    For now you can manage your <a href="/portfolio">portfolio</a> 
    adding your <a href="/transactions">transactions</a>, set your 
    <a href="/notifications">notification alerts</a>, within other 
    <a href="https://github.com/pantunes/xtcryptosignals/blob/master/CHANGELOG.md">features</a>.
    <br><br>
    Keyboard shortcuts:
    <ul>
    <li>ALT + L: Login</li>
    <li>ALT + C: Contact</li>
    <li>ALT + S: Signup</li>
    <li>ALT + SPACE: Activate Spotlight. Search anything in the Platform</li>
    </ul>
    In case you are curious about further feature releases Watch/Star this 
    Project <a href="https://github.com/pantunes/xtcryptosignals">here</a>.
    <br/><br/>
    We hope you like this platform experience and please drop us some 
    <a href="javascript:open_modal('#contact');">lines</a>
     in case of any question.
    <br/><br/>
    The <code>XTCryptoSignals</code> Team
    """
    )


@bp.route("/signup", methods=["POST"])
def signup():
    form_data = request.form.to_dict()

    try:
        if form_data["captcha"] != session["captcha"]:
            return dict(error="Bad Captcha."), 404
    except KeyError:
        return dict(error="Bad Captcha."), 404

    response = requests.post(
        url=f"{current_app.config['SERVER_API_BASE_URL']}signup",
        json=form_data,
    )

    _json = response.json()

    if response.status_code == 200:
        login_user(Auth(_json))

    return _json, response.status_code
