__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"

from xtcryptosignals.server.migrations import AddProjectMigration


class Migration(AddProjectMigration):
    PROJECTS = dict(
        ICP=dict(
            name="Dfinity",
            website="https://dfinity.org",
            twitter="https://twitter.com/dfinity",
            wikipedia="https://en.wikipedia.org/wiki/Dfinity",
        ),
    )
