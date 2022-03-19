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
        RLC=dict(
            name="iExec RLC",
            website="https://iex.ec",
            twitter="https://twitter.com/iEx_ec",
            wikipedia=None,
        ),
        SNX=dict(
            name="Synthetix",
            website="https://www.synthetix.io",
            twitter="https://twitter.com/synthetix_io",
            wikipedia=None,
        ),
    )
