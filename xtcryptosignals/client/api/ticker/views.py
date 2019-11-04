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
)
from xtcryptosignals import settings as s
from xtcryptosignals import __version__
from xtcryptosignals.client.utils import (
    validate_args,
    get_pairs,
    get_tokens,
)


bp = Blueprint('ticker', __name__)


_COLUMN_ATTRIBUTES = [
    'Price', 'Price Change', 'Volume 24h',
    'Volume Change', 'Number Trades 24h',
    'Number Trades Change', 'Updated On',
    'Price Change Chart',
]


@bp.context_processor
def before_request():
    return dict(
        server_api_base_url=current_app.config['SERVER_API_BASE_URL'],
        version=__version__,
        ga_tracking_id=current_app.config['GA_TRACKING_ID'],
        frequencies=s.HISTORY_FREQUENCY,
        pairs=get_pairs(),
        tokens=get_tokens(),
    )


@bp.route('/ticker/<frequency>')
@validate_args()
def ticker(frequency):
    return dict(
        template_name_or_list='ticker/ticker.html',
        symbols_per_exchange=s.SYMBOLS_PER_EXCHANGE,
        attributes=_COLUMN_ATTRIBUTES,
        frequency=frequency,
    )


@bp.route('/ticker/<pair>/<frequency>')
@validate_args()
def pair_frequency(pair, frequency):
    x = deepcopy(s.SYMBOLS_PER_EXCHANGE)
    pair_not_found = True
    for idx, i in enumerate(s.SYMBOLS_PER_EXCHANGE):
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
    x = deepcopy(s.SYMBOLS_PER_EXCHANGE)
    token_not_found = True
    _token = token.upper()
    for idx, i in enumerate(s.SYMBOLS_PER_EXCHANGE):
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
    return dict(
        tokens=get_tokens()
    )
