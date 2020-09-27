__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from mongodb_migrations.base import BaseMigration
from xtcryptosignals.common.utils import use_mongodb
from xtcryptosignals.server.api.projects.models import Project
from xtcryptosignals.tasks import settings as s


PROJECTS = dict(
    KNC=dict(
        name="Kyber Network",
        website="https://kyber.network",
        twitter="https://twitter.com/kybernetwork",
        wikipedia=None,
    ),
    LEND=dict(
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


class Migration(BaseMigration):
    @use_mongodb(db=s.MONGODB_NAME, host=s.MONGODB_HOST, port=s.MONGODB_PORT)
    def upgrade(self):
        for k, v in PROJECTS.items():
            Project(**{**{"coin_or_token": k}, **v}).save()
            print(f"Adding Project: {k}")

    def downgrade(self):
        pass
