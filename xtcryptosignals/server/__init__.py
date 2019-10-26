__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from flask import Flask
from flask_session import Session
from flask_socketio import SocketIO
from mongoengine import connect


app = Flask(__name__)

if app.config['ENV'] == "production":
    app.config.from_object("xtcryptosignals.server.config.ConfigProduction")
    app.config.from_pyfile('settings.prod.py')
else:
    app.config.from_object("xtcryptosignals.server.config.ConfigDevelopment")
    app.config.from_pyfile('settings.dev.py')


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

    connect(
        db=app.config['MONGODB_NAME'],
        host=app.config['MONGODB_HOST'],
        port=app.config['MONGODB_PORT']
    )

    sess.init_app(app)

    socketio.init_app(
        app=app,
        message_queue=app.config['BROKER_URL'],
        cors_allowed_origins=app.config['CORS_ALLOWED_ORIGINS']
    )

    return app
