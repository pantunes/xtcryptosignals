__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from flask_login import UserMixin


class Auth(UserMixin):
    def __init__(self, _json):
        self.id = _json['token']
        self.user = _json['user']

    def __repr__(self):
        return "%s" % (self.user['email'])
