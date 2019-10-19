__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from flask import Flask
import xtcryptosignals.settings as s


app = Flask(
    import_name=__name__,
    template_folder='../templates',
    # Note: let nginx or other more resourceful WS serve static content
    static_folder='../static',
)
app.config['TEMPLATES_AUTO_RELOAD'] = s.DEBUG
app.jinja_env.auto_reload = s.DEBUG


def create_app():
    from xtcryptosignals.client.common.views import bp as bp_common
    from xtcryptosignals.client.ticker.views import bp as bp_ticker
    from xtcryptosignals.client.contact.views import bp as bp_contact

    bps = (
        bp_ticker,
        bp_contact,
        bp_common,
    )

    for x in bps:
        app.register_blueprint(x)

    return app
