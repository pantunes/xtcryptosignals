__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests
from datetime import datetime
from mongodb_migrations.base import BaseMigration
from xtcryptosignals.common.utils import use_mongodb
from xtcryptosignals.tasks.models.cfgi import CFGI
from xtcryptosignals.tasks import settings as s


class Migration(BaseMigration):
    @use_mongodb(db=s.MONGODB_NAME, host=s.MONGODB_HOST, port=s.MONGODB_PORT)
    def upgrade(self):
        response = requests.get(url="{}/?limit=180".format(s.URL_CFGI))
        for i, x in enumerate(response.json()["data"]):
            index = x["value"]
            added_on = datetime.fromtimestamp(int(x["timestamp"])).date()
            kwargs = dict(index=index, added_on=added_on)
            CFGI(**kwargs).save()
            print("Adding CFGI: {index} {added_on}".format(**kwargs))

    def downgrade(self):
        pass
