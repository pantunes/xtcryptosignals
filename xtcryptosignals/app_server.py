__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import os
from flasgger import Swagger
from mongodb_migrations.cli import MigrationManager
from xtcryptosignals.config import settings as s
from xtcryptosignals.server import create_app, socketio


app = create_app()

migration_manager = MigrationManager()

migration_manager.config.mongo_database = s.MONGODB_NAME
migration_manager.config.mongo_port = s.MONGODB_PORT
migration_manager.config.mongo_migrations_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'server', 'migrations'
)
migration_manager.config.metastore = '_migrations'


def main():
    """
    Start RESTFul API and socketIO servers.
    """
    Swagger(app)

    migration_manager.run()

    socketio.run(
        app=app,
        debug=s.DEBUG,
        use_reloader=s.DEBUG,
        host=s.IP_ADDRESS,
        port=s.PORT_SERVER,
    )
