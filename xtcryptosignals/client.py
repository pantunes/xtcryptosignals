__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from flask import Flask, render_template


DEBUG = True

app = Flask(__name__)
if DEBUG:
    app.jinja_env.auto_reload = DEBUG
    app.config['TEMPLATES_AUTO_RELOAD'] = DEBUG


@app.route('/')
def root():
    return render_template('index.html')


app.run(debug=DEBUG, port=8000, host='0.0.0.0')
