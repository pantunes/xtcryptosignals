__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from copy import deepcopy
from flask import (
    Blueprint,
    current_app,
    g,
)
from xtcryptosignals.client import service
from xtcryptosignals import __version__
from xtcryptosignals.client.utils import validate_args
from xtcryptosignals.common.utils import (
    get_pairs,
    get_coin_tokens,
)


bp = Blueprint('ticker', __name__)


_COLUMN_ATTRIBUTES = [
    'Price', 'Price Change', 'Volume 24h',
    'Volume Change', 'Number Trades 24h',
    'Number Trades Change', 'Updated On',
    'Price Change Chart',
]


@bp.before_request
def before_request():
    g.SYMBOLS_PER_EXCHANGE, _ = service.get_symbols_per_exchange()
    g.HISTORY_FREQUENCY, _ = service.get_history_frequency()


@bp.context_processor
def context_processor():
    return dict(
        socket_base_url=current_app.config['SOCKET_BASE_URL'],
        version=__version__,
        ga_tracking_id=current_app.config['GA_TRACKING_ID'],
        frequencies=g.HISTORY_FREQUENCY,
        pairs=get_pairs(g.SYMBOLS_PER_EXCHANGE),
        tokens=get_coin_tokens(g.SYMBOLS_PER_EXCHANGE),
    )


@bp.route('/ticker/<frequency>')
@validate_args()
def ticker(frequency):
    return dict(
        template_name_or_list='ticker/ticker.html',
        symbols_per_exchange=g.SYMBOLS_PER_EXCHANGE,
        attributes=_COLUMN_ATTRIBUTES,
        frequency=frequency,
    )


@bp.route('/ticker/<pair>/<frequency>')
@validate_args()
def pair_frequency(pair, frequency):
    x = deepcopy(g.SYMBOLS_PER_EXCHANGE)
    pair_not_found = True
    for idx, i in enumerate(g.SYMBOLS_PER_EXCHANGE):
        for a, b in i.items():
            x[idx][a]['pairs'] = []
            for c, d in b['pairs']:
                if c + d == pair.upper():
                    pair_not_found = False
                    x[idx][a]['pairs'] = [(c, d)]
                    break
    if pair_not_found:
        raise ValueError('Pair not found.')
    return dict(
        template_name_or_list='ticker/pair_frequency.html',
        symbols_per_exchange=x,
        attributes=_COLUMN_ATTRIBUTES,
        frequency=frequency,
        pair=pair.upper(),
    )


@bp.route('/ticker/source/<token>/<frequency>')
@validate_args()
def token_frequency(token, frequency):
    x = deepcopy(g.SYMBOLS_PER_EXCHANGE)
    token_not_found = True
    _token = token.upper()
    for idx, i in enumerate(g.SYMBOLS_PER_EXCHANGE):
        for a, b in i.items():
            x[idx][a]['pairs'] = []
            for c, d in b['pairs']:
                if c == _token:
                    token_not_found = False
                    x[idx][a]['pairs'].append((c, d))
    if token_not_found:
        raise ValueError('Token not found.')
    return dict(
        template_name_or_list='ticker/token_frequency.html',
        symbols_per_exchange=x,
        attributes=_COLUMN_ATTRIBUTES,
        frequency=frequency,
        token=_token,
    )


@bp.route('/ticker/tokens')
def tokens():
    return dict(tokens=get_coin_tokens(g.SYMBOLS_PER_EXCHANGE)), 200


@bp.route('/ticker/frequencies')
def frequencies():
    return dict(frequencies=g.HISTORY_FREQUENCY), 200
