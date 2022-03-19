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
        KNC=dict(
            name="Kyber Network",
            website="https://kyber.network",
            twitter="https://twitter.com/kybernetwork",
            wikipedia=None,
        ),
        AAVE=dict(
            name="Aave",
            website="https://aave.com",
            twitter="https://twitter.com/aaveaave",
            wikipedia=None,
        ),
        REN=dict(
            name="Ren",
            website="https://renproject.io",
            twitter="https://twitter.com/renprotocol",
            wikipedia=None,
        ),
    )
