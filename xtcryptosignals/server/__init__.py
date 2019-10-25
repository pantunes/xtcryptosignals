__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from redis import Redis
from flask import Flask
from flask_session import Session
from flask_socketio import SocketIO
from xtcryptosignals import (
    __title__,
    __version__,
    __description__,
)
from xtcryptosignals.config.celeryconfig import BROKER_URL
import xtcryptosignals.config.settings as s


app = Flask(__name__)

app.config['SECRET_KEY'] = s.SECRET_KEY

app.config['SWAGGER'] = {
    "info": {
        "title": __title__,
        "version": __version__,
        "description": __description__,
    },
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header"
        }
    },
    "specs": [
        {
            "endpoint": 'apispec_xtcryptosignals',
            "route": '/apispec_xtcryptosignals.json',
        }
    ],
}

app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = Redis(host='localhost', port=6379)


sess = Session()

socketio = SocketIO()


def create_app():
    from xtcryptosignals.server.api.ticker import views
    from xtcryptosignals.server.api.contact.views import bp as bp_contact
    from xtcryptosignals.server.api.auth.views import bp as bp_auth
    from xtcryptosignals.server.api.user.views import bp as bp_user

    bps = (
        bp_auth,
        bp_user,
        bp_contact,
    )

    for x in bps:
        app.register_blueprint(x)

    sess.init_app(app)

    socketio.init_app(
        app=app,
        message_queue=BROKER_URL,
        cors_allowed_origins=s.CORS_ALLOWED_ORIGINS,
    )

    return app
