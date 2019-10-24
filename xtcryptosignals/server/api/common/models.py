__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from datetime import datetime
from mongoengine import Document, DateTimeField


def _set_timestamp(x):
    utc_now = datetime.utcnow()
    if not x.created_on:
        x.created_on = utc_now
    else:
        x.modified_on = utc_now


class DocumentValidation(Document):
    created_on = DateTimeField(required=True)
    modified_on = DateTimeField()

    meta = {
        'abstract': True,
        'allow_inheritance': True,
    }

    _pre_save_hooks = ()

    def save(self, *args, **kwargs):
        for hook in self._pre_save_hooks:
            hook(self)
        _set_timestamp(self)
        return super(DocumentValidation, self).save(*args, **kwargs)

    def to_dict(self):
        e = {}
        for k in self._fields.keys():
            if self[k] is None:
                continue
            if k == 'id':
                e['_id'] = self[k]
                continue
            e[k] = self[k]
        return e
