__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from flask import Flask, render_template
import xtcryptosignals.settings as s


app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'
if s.DEBUG:
    app.jinja_env.auto_reload = s.DEBUG
    app.config['TEMPLATES_AUTO_RELOAD'] = s.DEBUG


@app.route('/')
def root():
    return render_template('index.html')


def main():
    """
    Start web client
    """
    app.run(debug=s.DEBUG, port=8000, host='0.0.0.0')
