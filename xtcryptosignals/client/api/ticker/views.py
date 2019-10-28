__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import random
from copy import deepcopy
from flask import (
    request,
    render_template,
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
def server_api_base_url():
    data = dict(
        server_api_base_url=current_app.config['SERVER_API_BASE_URL'],
        version=__version__,
        ga_tracking_id=current_app.config['GA_TRACKING_ID'],
        frequencies=s.HISTORY_FREQUENCY,
        frequency_lower=s.TICKER_SCHEDULE,
    )
    if request.path != '/':
        data.update(
            pairs=get_pairs(),
            tokens=get_tokens(),
        )
    return data


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


@bp.route('/ticker/<frequency>')
@validate_args()
def ticker(frequency):
    return dict(
        template_name_or_list='ticker.html',
        symbols_per_exchange=s.SYMBOLS_PER_EXCHANGE,
        attributes=_COLUMN_ATTRIBUTES,
        frequency=frequency,
    )


@bp.route('/ticker/<pair>/<frequency>')
@validate_args()
def ticker_pair(pair, frequency):
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
        template_name_or_list='ticker_pair.html',
        symbols_per_exchange=x,
        attributes=_COLUMN_ATTRIBUTES,
        frequency=frequency,
        pair=pair.upper(),
    )


@bp.route('/ticker/source/<token>/<frequency>')
@validate_args()
def ticker_token(token, frequency):
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
        template_name_or_list='ticker_token.html',
        symbols_per_exchange=x,
        attributes=_COLUMN_ATTRIBUTES,
        frequency=frequency,
        token=_token,
    )
