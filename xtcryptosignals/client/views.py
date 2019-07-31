__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import random
import requests
from copy import deepcopy
from flask import Flask, request, render_template
import xtcryptosignals.settings as s
from xtcryptosignals import __version__
from xtcryptosignals.client.service import (
    validate_args, get_pairs,
)


app = Flask(
    import_name=__name__,
    template_folder='../templates',
    # Note: let nginx or other more resourceful WS serve static content
    static_folder='../static',
)
app.config['TEMPLATES_AUTO_RELOAD'] = s.DEBUG
app.jinja_env.auto_reload = s.DEBUG


_COLUMN_ATTRIBUTES = [
    'Price', 'Price Change', 'Volume 24h',
    'Volume Change', 'Number Trades 24h',
    'Number Trades Change', 'Updated On',
    'Price Change Chart',
]


@app.context_processor
def server_api_base_url():
    return dict(
        server_api_base_url=s.SERVER_API_BASE_URL,
        version=__version__,
    )


@app.route('/')
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
        frequencies=s.HISTORY_FREQUENCY,
    )


@app.route('/ticker/<frequency>')
@validate_args()
def ticker(frequency):
    return dict(
        template_name_or_list='ticker.html',
        symbols_per_exchange=s.SYMBOLS_PER_EXCHANGE,
        attributes=_COLUMN_ATTRIBUTES,
        frequencies=s.HISTORY_FREQUENCY,
        frequency=frequency,
        pairs=get_pairs(),
    )


@app.route('/ticker/<pair>/<frequency>')
@validate_args()
def ticker_pair(pair, frequency):
    x = deepcopy(s.SYMBOLS_PER_EXCHANGE)
    pair_not_found = True
    for idx, i in enumerate(s.SYMBOLS_PER_EXCHANGE):
        for a, b in i.items():
            for c, d in b['pairs']:
                if c + d == pair.upper():
                    pair_not_found = False
                    x[idx][a]['pairs'] = [(c, d)]
                    break
            else:
                x[idx][a]['pairs'] = []
    if pair_not_found:
        raise ValueError('Pair not found')
    return dict(
        template_name_or_list='ticker_pair.html',
        symbols_per_exchange=x,
        attributes=_COLUMN_ATTRIBUTES,
        frequencies=s.HISTORY_FREQUENCY,
        frequency=frequency,
        pairs=get_pairs(),
        pair=pair,
    )


@app.route('/contact', methods=['POST'])
def contact():
    r = requests.post(
        '{}contact'.format(s.SERVER_API_BASE_URL), data=request.form
    )
    return r.text, r.status_code


@app.errorhandler(404)
def page_not_found(_):
    return render_template(
        template_name_or_list='error.html',
        error='The URL is incorrect'
    ), 404
