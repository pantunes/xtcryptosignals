__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from functools import wraps
from mongoengine import connect
from flask_socketio import disconnect
from flask_login import current_user
import xtcryptosignals.settings as s


def use_mongodb(**config_params):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            connect(s.MONGODB_NAME, **config_params)
            return f(*args, **kwargs)
        return wrapper
    return decorator


def authenticated(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            disconnect()
        else:
            return f(*args, **kwargs)
    return wrapped
