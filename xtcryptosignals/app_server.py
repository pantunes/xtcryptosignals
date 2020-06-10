__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import click
from xtcryptosignals.server import create_app, socketio


app = create_app()


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.option(
    "--port",
    "-p",
    default=app.config["PORT"],
    help="The Server port to bind to",
)
def main(port):
    """
    Start RESTFul API and socketIO servers.
    """
    socketio.run(
        app=app,
        debug=app.config["DEBUG"],
        use_reloader=app.config["DEBUG"],
        host=app.config["IP_ADDRESS"],
        port=port,
    )
