__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import click
from xtcryptosignals.prod.wsgi import start
from xtcryptosignals.client import create_app


app = create_app()


@click.command(
    context_settings=dict(help_option_names=['-h', '--help'])
)
@click.option(
    '--num-workers',
    help='Enables Production environment with the given number of workers'
)
@click.pass_context
def main(ctx, num_workers):
    """
    Start web client
    """
    port = app.config['PORT']
    host = app.config['IP_ADDRESS']

    if num_workers:
        start(handler=app, host=host, port=port, num_workers=num_workers)
        ctx.exit()

    app.run(debug=app.config['DEBUG'], host=host, port=port)
