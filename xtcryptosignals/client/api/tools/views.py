__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from datetime import datetime
from flask import (
    Blueprint,
    current_app,
    render_template,
    g,
)
from xtcryptosignals.client import service
from xtcryptosignals import __version__
from xtcryptosignals.common.utils import (
    get_pairs,
    get_coin_tokens,
)


bp = Blueprint('tools', __name__)


@bp.before_request
def before_request():
    g.SYMBOLS_PER_EXCHANGE, _ = service.get_symbols_per_exchange()
    g.HISTORY_FREQUENCY, _ = service.get_history_frequency()


@bp.context_processor
def context_processor():
    return dict(
        version=__version__,
        ga_tracking_id=current_app.config['GA_TRACKING_ID'],
        current_year=datetime.utcnow().year,
        frequencies=g.HISTORY_FREQUENCY,
        pairs=get_pairs(g.SYMBOLS_PER_EXCHANGE),
        tokens=get_coin_tokens(g.SYMBOLS_PER_EXCHANGE),
    )


@bp.route('/tools/fear-and-greed')
def fear_and_greed():
    _min = g.HISTORY_FREQUENCY.index(current_app.config['CFGI_MIN'])
    _max = g.HISTORY_FREQUENCY.index(current_app.config['CFGI_MAX'])
    chart_frequencies = g.HISTORY_FREQUENCY[_min:_max]
    return render_template(
        template_name_or_list='tools/fear-and-greed.html',
        frequency=current_app.config['CFGI_MIN'],
        chart_frequencies=chart_frequencies,
    )
