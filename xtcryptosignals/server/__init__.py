__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from flask import Flask
from flask_socketio import SocketIO
from xtcryptosignals import (
    __title__,
    __version__,
    __description__,
)
from xtcryptosignals.celeryconfig import BROKER_URL
import xtcryptosignals.settings as s


app = Flask(__name__)


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


socketio = SocketIO()


def create_app():
    from xtcryptosignals.server.messaging import views
    from xtcryptosignals.server.contact.views import bp as bp_contact

    bps = (
        bp_contact,
    )

    for x in bps:
        app.register_blueprint(x)

    socketio.init_app(
        app=app,
        message_queue=BROKER_URL,
        cors_allowed_origins=s.CORS_ALLOWED_ORIGINS,
    )

    return app
