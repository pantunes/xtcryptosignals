__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests
from xtcryptosignals.client import login_manager
from xtcryptosignals.client.api.auth.models import Auth
from xtcryptosignals.config import settings as s


@login_manager.user_loader
def load_user(token):
    response = requests.get(
        url='{}auth'.format(s.SERVER_API_BASE_URL),
        headers=dict(
            Authorization=token
        )
    )

    if response.status_code != 200:
        return

    _json = response.json()
    return Auth(_json)
