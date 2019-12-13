__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import os
import click
from flasgger import Swagger
from mongodb_migrations.cli import MigrationManager
from xtcryptosignals.server import create_app, socketio


app = create_app()


migration_manager = MigrationManager()

migration_manager.config.mongo_database = app.config['MONGODB_NAME']
migration_manager.config.mongo_port = app.config['MONGODB_PORT']
migration_manager.config.mongo_migrations_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'server', 'migrations'
)
migration_manager.config.metastore = '_migrations'


@click.command(
    context_settings=dict(help_option_names=['-h', '--help'])
)
@click.option(
    '--port', '-p',
    default=app.config['PORT'],
    help='The Server port to bind to'
)
def main(port):
    """
    Start RESTFul API and socketIO servers.
    """
    Swagger(app)

    migration_manager.run()

    socketio.run(
        app=app,
        debug=app.config['DEBUG'],
        use_reloader=app.config['DEBUG'],
        host=app.config['IP_ADDRESS'],
        port=port,
    )
