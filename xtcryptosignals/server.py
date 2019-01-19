__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import eventlet
from flask import Flask, jsonify
from flask_socketio import SocketIO
from xtcryptosignals.celeryconfig import BROKER_URL

eventlet.monkey_patch()


app = Flask(__name__)
socketio = SocketIO(app, message_queue=BROKER_URL)


@app.route('/')
def root():
    return jsonify(dict(status='Ok'))


@socketio.on('connect')
def on_connect():
    print('on_connect')


@socketio.on('disconnect')
def on_disconnect():
    print('on_disconnect')


socketio.run(app, debug=False, port=5000, host='0.0.0.0')
