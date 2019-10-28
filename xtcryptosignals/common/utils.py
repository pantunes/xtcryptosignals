__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from functools import wraps
from mongoengine import connect


def use_mongodb(**config_params):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            connect(**config_params)
            return f(*args, **kwargs)
        return wrapper
    return decorator
