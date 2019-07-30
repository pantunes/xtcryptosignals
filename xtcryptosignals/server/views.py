__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import os
import eventlet
from datetime import datetime
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, Namespace
import xtcryptosignals.settings as s
from xtcryptosignals.celeryconfig import BROKER_URL
from xtcryptosignals.server.service import (
    get_ticker_data_from_namespace,
    use_mongodb,
)


eventlet.monkey_patch()


app = Flask(__name__)
socketio = SocketIO(app, message_queue=BROKER_URL)

users_per_namespace = {'/'+x: 0 for x in s.HISTORY_FREQUENCY}
users_per_namespace.update({'/': 0})


@socketio.on('connect')
def on_general_connect():
    global users_per_namespace
    users_per_namespace['/'] += 1
    socketio.emit('general', users_per_namespace, broadcast=True)


@socketio.on('disconnect')
def on_general_disconnect():
    global users_per_namespace
    users_per_namespace['/'] -= 1
    socketio.emit('general', users_per_namespace, broadcast=True)


class TickerSockeIONamespace(Namespace):
    @use_mongodb()
    def on_connect(self):
        global users_per_namespace
        users_per_namespace[self.namespace] += 1
        rows = get_ticker_data_from_namespace(self.namespace)
        for row in rows:
            socketio.emit('ticker', row, namespace=self.namespace)
        socketio.emit('general', users_per_namespace, broadcast=True)

    def on_disconnect(self):
        global users_per_namespace
        users_per_namespace[self.namespace] -= 1
        socketio.emit('general', users_per_namespace, broadcast=True)


for x in s.HISTORY_FREQUENCY:
    socketio_model = type(
        'SocketIONamespace{}'.format(x), (TickerSockeIONamespace,), {}
    )
    socketio.on_namespace(socketio_model('/{}'.format(x)))


@app.route('/contact', methods=['POST'])
def contact():
    with open(os.path.join('/tmp', 'contact.csv'), 'a') as f:
        f.write("{}\t{}\t{}\t{}\n".format(
            str(datetime.utcnow()),
            request.form.get('email'),
            request.form.get('reason'),
            request.form.get('message').replace(
                '\r\n', ' '
            ).replace(
                '\n', ' '
            ))
        )
    return 'OK'
