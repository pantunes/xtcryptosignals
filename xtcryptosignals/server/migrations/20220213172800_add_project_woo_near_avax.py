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
        WOO=dict(
            name="WOO Network",
            website="https://woo.org",
            twitter="https://twitter.com/WOOnetwork",
        ),
        NEAR=dict(
            name="NEAR Protocol",
            website="https://near.org",
            twitter="https://twitter.com/nearprotocol",
        ),
        AVAX=dict(
            name="Avalanche",
            website="https://www.avax.network",
            twitter="https://twitter.com/avalancheavax",
        ),
    )
