__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import random
from flask import (
    render_template,
    Blueprint,
    current_app,
)
from xtcryptosignals import settings as s
from xtcryptosignals import __version__


bp = Blueprint('home', __name__)


@bp.context_processor
def before_request():
    return dict(
        server_api_base_url=current_app.config['SERVER_API_BASE_URL'],
        version=__version__,
        ga_tracking_id=current_app.config['GA_TRACKING_ID'],
        frequencies=s.HISTORY_FREQUENCY,
        frequency_lower=s.TICKER_SCHEDULE,
    )


@bp.route('/')
def index():
    symbols_per_exchange = []
    for x in s.SYMBOLS_PER_EXCHANGE:
        for exchange, item in x.items():
            if not item['pairs']:
                continue
            random_list = [x[0]+x[1] for x in item['pairs']]
            random.shuffle(random_list)
            symbols_per_exchange.append(
                {exchange: random_list[:3]}
            )
    return render_template(
        template_name_or_list='index.html',
        symbols_per_exchange=symbols_per_exchange,
    )
