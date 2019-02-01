__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import random
from copy import deepcopy
from flask import Flask, render_template
import xtcryptosignals.settings as s
from xtcryptosignals import __version__

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'
app.config['TEMPLATES_AUTO_RELOAD'] = s.DEBUG
app.jinja_env.auto_reload = s.DEBUG


_COLUMN_ATTRIBUTES = [
    'Price', 'Price Change Percent', 'Volume 24h',
    'Volume Change Percent', 'Number Trades 24h',
    'Number Trades Change Percent', 'Created On'
]


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
        'index.html',
        version=__version__,
        symbols_per_exchange=symbols_per_exchange,
        frequency=", ".join(s.HISTORY_FREQUENCY),
    )


@app.route('/io/ticker/<frequency>')
def ticker(frequency):
    return render_template(
        'ticker.html',
        symbols_per_exchange=s.SYMBOLS_PER_EXCHANGE,
        attributes=_COLUMN_ATTRIBUTES,
        frequency=frequency,
    )


@app.route('/io/ticker/<pair>/<frequency>')
def ticker_pair(pair, frequency):
    x = deepcopy(s.SYMBOLS_PER_EXCHANGE)
    for idx, i in enumerate(s.SYMBOLS_PER_EXCHANGE):
        for a, b in i.items():
            for c, d in b['pairs']:
                if c + d == pair.upper():
                    x[idx][a]['pairs'] = [(c, d)]
                    break
            else:
                x[idx][a]['pairs'] = []
    return render_template(
        'ticker_pair.html',
        symbols_per_exchange=x,
        attributes=_COLUMN_ATTRIBUTES,
        frequency=frequency,
        pair=pair,
    )


def main():
    """
    Start web client
    """
    app.run(debug=s.DEBUG, port=8000, host='0.0.0.0')
