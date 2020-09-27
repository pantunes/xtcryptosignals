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
    LINK=dict(
        name="Chainlink",
        website="https://chain.link",
        twitter="https://twitter.com/chainlink",
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
