__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests
from datetime import datetime
from flask import (
    Blueprint,
    current_app,
    g,
)
from flask_login import (
    login_required,
    current_user,
)
from xtcryptosignals.client import service
from xtcryptosignals import __version__
from xtcryptosignals.client.utils import validate_args
from xtcryptosignals.common.utils import (
    get_pairs,
    get_coin_tokens,
)


bp = Blueprint("exchange", __name__)


@bp.before_request
def before_request():
    g.SYMBOLS_PER_EXCHANGE, _ = service.get_symbols_per_exchange()
    g.HISTORY_FREQUENCY, _ = service.get_history_frequency()


@bp.context_processor
def context_processor():
    return dict(
        socket_base_url=current_app.config["SOCKET_BASE_URL"],
        version=__version__,
        ga_tracking_id=current_app.config["GA_TRACKING_ID"],
        current_year=datetime.utcnow().year,
        frequencies=g.HISTORY_FREQUENCY,
        pairs=get_pairs(g.SYMBOLS_PER_EXCHANGE),
        tokens=get_coin_tokens(g.SYMBOLS_PER_EXCHANGE, show_all=True),
        attributes={"price_usdt": "Price USDT"},
        frequency=g.HISTORY_FREQUENCY[0],
    )


@bp.route("/exchange/<exchange>", methods=["GET"])
@login_required
@validate_args()
def index(exchange):
    if exchange != "binance":
        raise ValueError("Exchange not supported for now.")

    return dict(exchange=exchange, template_name_or_list="exchange.html")


bp_xhr = Blueprint("exchange/xhr", __name__)


@bp_xhr.route("/exchange/<exchange>/balance", methods=["GET"])
@login_required
def balance(exchange):
    response = requests.get(
        url=f"{current_app.config['SERVER_API_BASE_URL']}exchange/{exchange}/balance",
        headers=dict(Authorization=current_user.id),
    )
    return response.json(), response.status_code


@bp_xhr.route("/exchange/<exchange>/orders/open", methods=["GET"])
@login_required
def open_orders(exchange):
    response = requests.get(
        url=f"{current_app.config['SERVER_API_BASE_URL']}exchange/{exchange}/orders/open",
        headers=dict(Authorization=current_user.id),
    )
    return response.json(), response.status_code


@bp_xhr.route("/exchange/<exchange>/account/status", methods=["GET"])
@login_required
def account_status(exchange):
    response = requests.get(
        url=f"{current_app.config['SERVER_API_BASE_URL']}exchange/{exchange}/account/status",
        headers=dict(Authorization=current_user.id),
    )
    return response.json(), response.status_code
