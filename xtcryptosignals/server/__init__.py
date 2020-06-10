__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from flask import Flask
from flask_session import Session
from flask_socketio import SocketIO
from flasgger import Swagger
from mongoengine import connect


app = Flask(__name__)

try:
    app.config.from_object(
        f"xtcryptosignals.server.config.Config{app.config['ENV'].title()}"
    )
except ImportError:
    raise ValueError("Unknown FLASK_ENV")

app.config.from_envvar("SETTINGS_APP")


sess = Session()
socketio = SocketIO()


def create_app():
    from xtcryptosignals.server.api.tickers import views
    from xtcryptosignals.server.api.contact.views import bp as bp_contact
    from xtcryptosignals.server.api.auth.views import bp as bp_auth
    from xtcryptosignals.server.api.user.views import bp as bp_user
    from xtcryptosignals.server.api.tokens.views import bp as bp_tokens
    from xtcryptosignals.server.api.portfolio.views import bp as bp_portfolio
    from xtcryptosignals.server.api.parties.views import bp as bp_parties
    from xtcryptosignals.server.api.charts.views import bp as bp_charts
    from xtcryptosignals.server.api.notifications.views import (
        bp as bp_notification,
    )
    from xtcryptosignals.server.api.transactions.views import (
        bp as bp_transaction,
    )
    from xtcryptosignals.server.api.projects.views import bp as bp_projects

    bps = (
        bp_auth,
        bp_user,
        bp_contact,
        bp_tokens,
        bp_transaction,
        bp_notification,
        bp_portfolio,
        bp_parties,
        bp_charts,
        bp_projects,
    )

    for x in bps:
        app.register_blueprint(x)

    connect(
        db=app.config["MONGODB_NAME"],
        host=app.config["MONGODB_HOST"],
        port=app.config["MONGODB_PORT"],
    )

    sess.init_app(app)

    socketio.init_app(
        app=app,
        message_queue=app.config["BROKER_URL"],
        cors_allowed_origins=app.config["CORS_ALLOWED_ORIGINS"],
    )

    if app.config["SWAGGER"]:
        Swagger(app)

    return app
