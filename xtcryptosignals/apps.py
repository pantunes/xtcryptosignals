__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"

import click
import xtcryptosignals.settings as s
from xtcryptosignals.wsgi_gunicorn import start
from xtcryptosignals.client.views import app as app_client
from xtcryptosignals.server.views import socketio
from xtcryptosignals.client.views import app as app_server


@click.command(
    context_settings=dict(help_option_names=['-h', '--help'])
)
@click.option(
    '--gunicorn',
    is_flag=True,
    help="Enable production setup mode",
)
def main_client(gunicorn):
    """
    Start web client
    """
    port = s.PORT_CLIENT
    host = s.IP_ADDRESS

    if gunicorn:
        start(handler=app_client, host=host, port=port)
        return

    app_client.run(debug=s.DEBUG, host=host, port=port)


def main_server():
    """
    Start RESTFul server API and socketIO server.
    """
    import sys
    sys.argv = [sys.argv[0]]
    from xtcryptosignals.data_migrations import data_migrations_manager

    data_migrations_manager.run()

    socketio.run(
        app_server,
        debug=s.DEBUG,
        use_reloader=s.DEBUG,
        host=s.IP_ADDRESS,
        port=s.PORT_SERVER,
    )
