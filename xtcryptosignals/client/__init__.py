__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from flask import Flask
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect


app = Flask(
    import_name=__name__,
    template_folder='templates',
    # TODO @Note: let nginx or other more resourceful Load Balancer
    # serve static content within this folder.
    static_folder='static',
)

app.jinja_env.auto_reload = app.config['DEBUG']

if app.config['ENV'] == "production":
    app.config.from_object("xtcryptosignals.client.config.ConfigProduction")
else:
    app.config.from_object("xtcryptosignals.client.config.ConfigDevelopment")

app.config.from_envvar('SETTINGS_APP')


login_manager = LoginManager()

csrf = CSRFProtect()


def create_app():
    from xtcryptosignals.client.api.home.views import bp as bp_home
    from xtcryptosignals.client.api.auth.views import bp as bp_auth
    from xtcryptosignals.client.api.errors.views import bp as bp_errors
    from xtcryptosignals.client.api.ticker.views import bp as bp_ticker
    from xtcryptosignals.client.api.contact.views import bp as bp_contact
    from xtcryptosignals.client.api.user.views import bp as bp_user
    from xtcryptosignals.client.api.portfolio.views import bp as bp_portfolio
    from xtcryptosignals.client.api.notification.views import \
        bp as bp_notification
    from xtcryptosignals.client.api.transaction.views import \
        bp as bp_transaction

    bps = (
        bp_home,
        bp_auth,
        bp_user,
        bp_ticker,
        bp_contact,
        bp_errors,
        bp_portfolio,
        bp_notification,
        bp_transaction,
    )

    for x in bps:
        app.register_blueprint(x)

    login_manager.init_app(app)

    login_manager.login_view = "errors.logged_out"
    login_manager.session_protection = app.config['SESSION_PROTECTION']

    csrf.init_app(app)

    return app
