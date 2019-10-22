__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, _id):
        self.id = _id
        self.name = "TODO"

    def __repr__(self):
        return "%d/%s/" % (self.id, self.name)
