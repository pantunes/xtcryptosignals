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

bp = Blueprint("portfolio", __name__)


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
        show_donation=current_app.config["SHOW_DONATION"],
        frequencies=g.HISTORY_FREQUENCY,
        pairs=get_pairs(g.SYMBOLS_PER_EXCHANGE),
        tokens=get_coin_tokens(g.SYMBOLS_PER_EXCHANGE, show_all=True),
        attributes={"price_usdt": "Price USDT"},
    )


@bp.route("/portfolio", methods=["GET"])
@login_required
def index():
    return render_template(
        template_name_or_list="portfolio.html",
        frequency=g.HISTORY_FREQUENCY[0],
    )


bp_xhr = Blueprint("portfolio/xhr", __name__)


@bp_xhr.route("/portfolio/list", methods=["GET"])
@login_required
def _list():
    response = requests.get(
        url=f"{current_app.config['SERVER_API_BASE_URL']}portfolio",
        headers=dict(Authorization=current_user.id),
    )
    return response.json(), response.status_code
