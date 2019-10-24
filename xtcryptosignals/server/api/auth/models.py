__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from mongoengine import StringField, ReferenceField
from xtcryptosignals.server.api.common.models import DocumentValidation
from xtcryptosignals.server.api.user.models import User


class Auth(DocumentValidation):
    user = ReferenceField(User, required=True, unique=True)
    token = StringField(required=True, unique=True)

    meta = {
        'collection': 'auth',
        'indexes': ['token'],
    }

    def to_dict(self):
        e = super(Auth, self).to_dict()
        for k in self._fields.keys():
            if k == 'user':
                e[k] = self[k].to_dict()
                continue
        return e
