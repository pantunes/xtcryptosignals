__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"

import click
import xtcryptosignals.settings as s
from xtcryptosignals.wsgi_gunicorn import start
from xtcryptosignals.client.views import app


@click.command(
    context_settings=dict(help_option_names=['-h', '--help'])
)
@click.option(
    '--gunicorn',
    is_flag=True,
    help="Enable production setup mode",
)
def main(gunicorn):
    """
    Start web client
    """
    port = s.PORT_CLIENT
    host = s.IP_ADDRESS

    if gunicorn:
        start(handler=app, host=host, port=port)
        return

    app.run(debug=s.DEBUG, host=host, port=port)
