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
        SOL=dict(
            name="Solana",
            website="https://solana.com",
            twitter="https://twitter.com/solana",
            wikipedia="https://en.wikipedia.org/wiki/Solana_(blockchain_platform)",
        ),
        ATOM=dict(
            name="Cosmos",
            website="https://cosmos.network",
            twitter="https://twitter.com/cosmos",
        ),
    )
