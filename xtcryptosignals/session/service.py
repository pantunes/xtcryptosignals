__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from flask_login import UserMixin
from xtcryptosignals import settings as s


class User(UserMixin):
    def get_id(self):
        return s.X_API

    def __repr__(self):
        return '<API Key %r>' % s.X_API
