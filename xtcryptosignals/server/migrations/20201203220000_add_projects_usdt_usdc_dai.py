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
        USDT=dict(
            name="Tether",
            website="https://tether.to",
            twitter="https://twitter.com/Tether_to",
            wikipedia="https://en.wikipedia.org/wiki/Tether_(cryptocurrency)",
        ),
        USDC=dict(
            name="USD Coin",
            website="https://www.coinbase.com/usdc",
            twitter="https://twitter.com/coinbase",
            wikipedia="https://en.wikipedia.org/wiki/USD_Coin",
        ),
        DAI=dict(
            name="MakerDAO",
            website="https://makerdao.com",
            twitter="https://twitter.com/MakerDAO",
            wikipedia="https://en.wikipedia.org/wiki/MakerDAO",
        ),
    )
