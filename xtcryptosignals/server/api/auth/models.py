__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from mongoengine import (
    StringField,
    ReferenceField,
    BooleanField,
    IntField,
)
from xtcryptosignals.common.models import DocumentValidation
from xtcryptosignals.server.api.user.models import User


def _increment_num_logins(_self):
    if not _self.pk or not _self.active:
        return
    _self.num_logins += 1


class Auth(DocumentValidation):
    user = ReferenceField(User, required=True)
    token = StringField(required=True, unique=True)
    num_logins = IntField(default=1)
    active = BooleanField(default=True)

    _pre_save_hooks = (_increment_num_logins,)

    meta = {
        'collection': 'auth',
        'indexes': [{
            'fields': ('user', 'token', 'active',),
            'unique': True
        }]
    }

    def to_dict(self):
        e = super(Auth, self).to_dict()
        for k in self._fields.keys():
            if k == 'user':
                e[k] = self[k].to_dict()
                continue
        return e
