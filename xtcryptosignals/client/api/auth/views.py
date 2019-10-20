__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from xtcryptosignals.client import login_manager
from xtcryptosignals.client.api.auth.models import User


@login_manager.user_loader
def load_user(user_id):
    return User(1234)
