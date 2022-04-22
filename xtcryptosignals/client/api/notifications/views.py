__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from datetime import datetime

import requests
from flask import (
    Blueprint,
    render_template,
    current_app,
    request,
    g,
)
from flask_login import (
    login_required,
    current_user,
)

from xtcryptosignals import __version__
from xtcryptosignals.client import service
from xtcryptosignals.common.utils import (
    get_pairs,
    get_coin_tokens,
)

bp = Blueprint("notification", __name__)


@bp.context_processor
def context_processor():
    return dict(
        application_server_key=current_app.config["APPLICATION_SERVER_KEY"],
        version=__version__,
        ga_tracking_id=current_app.config["GA_TRACKING_ID"],
        current_year=datetime.utcnow().year,
        show_donation=current_app.config["SHOW_DONATION"],
        frequencies=g.HISTORY_FREQUENCY,
        pairs=get_pairs(g.SYMBOLS_PER_EXCHANGE),
        tokens=get_coin_tokens(g.SYMBOLS_PER_EXCHANGE, show_all=True),
    )


@bp.route("/notifications", methods=["GET"])
@login_required
def index():
    g.SYMBOLS_PER_EXCHANGE, _ = service.get_symbols_per_exchange()
    g.HISTORY_FREQUENCY, _ = service.get_history_frequency()
    return render_template(
        template_name_or_list="notification.html",
        frequency=g.HISTORY_FREQUENCY[0],
    )


bp_xhr = Blueprint("notification/xhr", __name__)


@bp_xhr.route("/notifications/list", methods=["GET"])
@login_required
def notifications():
    response = requests.get(
        url=f"{current_app.config['SERVER_API_BASE_URL']}notifications",
        headers=dict(Authorization=current_user.id),
        params=request.args,
    )
    return dict(results=response.json()), response.status_code


@bp_xhr.route("/notifications/rules", methods=["GET"])
@login_required
def rules():
    response = requests.get(
        url=f"{current_app.config['SERVER_API_BASE_URL']}notifications/rules",
        headers=dict(Authorization=current_user.id),
    )
    return dict(results=response.json()), response.status_code


@bp_xhr.route("/notifications/rule/add", methods=["POST"])
@login_required
def rule_add():
    response = requests.post(
        url=f"{current_app.config['SERVER_API_BASE_URL']}notifications/rule/add",
        headers=dict(Authorization=current_user.id),
        json=request.form.to_dict(),
    )
    return response.json(), response.status_code


@bp_xhr.route("/notifications/rule/<notification>/edit", methods=["POST"])
@login_required
def rule_edit(notification):
    response = requests.put(
        url=f"{current_app.config['SERVER_API_BASE_URL']}notifications/rule/{notification}",
        headers=dict(Authorization=current_user.id),
        json=request.form.to_dict(),
    )
    return response.json(), response.status_code


@bp_xhr.route("/notifications/rule/<notification>/delete", methods=["POST"])
@login_required
def rule_delete(notification):
    response = requests.delete(
        url=f"{current_app.config['SERVER_API_BASE_URL']}notifications/rule/{notification}",
        headers=dict(Authorization=current_user.id),
        json=request.form.to_dict(),
    )
    return {}, response.status_code


@bp_xhr.route("/notifications/rule/<notification>", methods=["GET"])
@login_required
def rule_get(notification):
    response = requests.get(
        url=f"{current_app.config['SERVER_API_BASE_URL']}notifications/rule/{notification}",
        headers=dict(Authorization=current_user.id),
        json=request.form.to_dict(),
    )
    return response.json(), response.status_code
