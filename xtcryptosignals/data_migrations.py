__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"

import os
from mongodb_migrations.cli import MigrationManager
from xtcryptosignals import settings as s


data_migrations_manager = MigrationManager()
data_migrations_manager.config.mongo_database = s.MONGODB_NAME
data_migrations_manager.config.mongo_migrations_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'migrations'
)
data_migrations_manager.config.metastore = '_database_migrations'
