__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import eventlet
from flask import Flask
from flask_socketio import SocketIO, Namespace
from flask_login import LoginManager
import xtcryptosignals.settings as s
from xtcryptosignals.celeryconfig import BROKER_URL
from xtcryptosignals.server.service import get_ticker_data_from_namespace
from xtcryptosignals.common.service import (
    use_mongodb,
    authenticated,
)
from xtcryptosignals.session.service import User


eventlet.monkey_patch()


app = Flask(__name__)

# socketIO
socketio = SocketIO(app, message_queue=BROKER_URL)

# session
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.request_loader
def load_user_from_request(request):
    # TODO
    print(request.args.get('X-API'))
    print(User().get_id())
    return User()


# pre-processing - active users
users_per_namespace = {'/'+x: 0 for x in s.HISTORY_FREQUENCY}
users_per_namespace.update({'/': 0})


@socketio.on('connect')
@authenticated
def on_general_connect():
    global users_per_namespace
    users_per_namespace['/'] += 1
    socketio.emit('general', users_per_namespace, broadcast=True)


@socketio.on('disconnect')
@authenticated
def on_general_disconnect():
    global users_per_namespace
    users_per_namespace['/'] -= 1
    socketio.emit('general', users_per_namespace, broadcast=True)


class TickerSockeIONamespace(Namespace):
    @use_mongodb()
    @authenticated
    def on_connect(self):
        global users_per_namespace
        users_per_namespace[self.namespace] += 1
        rows = get_ticker_data_from_namespace(self.namespace)
        for row in rows:
            socketio.emit('ticker', row, namespace=self.namespace)
        socketio.emit('general', users_per_namespace, broadcast=True)

    @authenticated
    def on_disconnect(self):
        global users_per_namespace
        users_per_namespace[self.namespace] -= 1
        socketio.emit('general', users_per_namespace, broadcast=True)


for x in s.HISTORY_FREQUENCY:
    socketio_model = type(
        'SocketIONamespace{}'.format(x), (TickerSockeIONamespace,), {}
    )
    socketio.on_namespace(socketio_model('/{}'.format(x)))


def main():
    """
    Start RESTFul server API and socketIO server.
    """
    socketio.run(
        app,
        debug=s.DEBUG,
        use_reloader=s.DEBUG,
        port=s.PORT_SERVER,
        host='0.0.0.0',
    )
