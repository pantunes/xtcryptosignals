__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import eventlet
from flask import Flask
from flask_socketio import SocketIO, Namespace
import xtcryptosignals.settings as s
from xtcryptosignals.celeryconfig import BROKER_URL
from xtcryptosignals.server.service import get_ticker_data_from_namespace
from xtcryptosignals.storage.service import use_mongodb


eventlet.monkey_patch()


app = Flask(__name__)
socketio = SocketIO(app, message_queue=BROKER_URL)


@socketio.on('connect')
def on_general_connect():
    print('on_connect /')


@socketio.on('disconnect')
def on_general_disconnect():
    print('on_disconnect /')


class RootSockeIONamespace(Namespace):
    @use_mongodb()
    def on_connect(self):
        print('on_connect ' + self.namespace)
        rows = get_ticker_data_from_namespace(self.namespace)
        for row in rows:
            socketio.emit('ticker', row, namespace=self.namespace)

    def on_disconnect(self):
        print('on_disconnect ' + self.namespace)


for x in s.HISTORY_FREQUENCY:
    socketio_model = type(
        'SockeIONamespace{}'.format(x), (RootSockeIONamespace,), {}
    )
    socketio.on_namespace(socketio_model('/{}'.format(x)))


def main():
    """
    Start RESTFul server API and socketIO server.
    """
    socketio.run(
        app, debug=s.DEBUG,
        use_reloader=s.DEBUG,
        port=s.PORT_SERVER,
        host='0.0.0.0',
    )
