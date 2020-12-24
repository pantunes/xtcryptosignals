__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from datetime import datetime
from flask import (
    request,
    render_template,
    Blueprint,
    current_app,
    g,
)
from xtcryptosignals.client import service
from xtcryptosignals import __version__


bp = Blueprint("home", __name__)


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
    )


@bp.route("/old", methods=["GET"])
@bp.route("/", methods=["GET"])
def index():
    filenames = {
        "/": 'landing.html',
        "/old": 'index.html',
    }
    return render_template(template_name_or_list=filenames[str(request.url_rule)])
