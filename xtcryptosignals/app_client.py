__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"

import click
import xtcryptosignals.settings as s
from xtcryptosignals.wsgi import start
from xtcryptosignals.client import create_app


app = create_app()


@click.command(
    context_settings=dict(help_option_names=['-h', '--help'])
)
@click.option(
    '--prod',
    is_flag=True,
    help="Enable production setup mode",
)
@click.pass_context
def main(ctx, prod):
    """
    Start web client
    """
    port = s.PORT_CLIENT
    host = s.IP_ADDRESS

    if prod:
        start(handler=app, host=host, port=port)
        ctx.exit()

    app.run(debug=s.DEBUG, host=host, port=port)
