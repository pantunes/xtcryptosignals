__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


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
    return render_template('index.html', version=__version__)


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
