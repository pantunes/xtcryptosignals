__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import xtcryptosignals.settings as s
from functools import wraps
from flask import render_template


def validate_args():
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if kwargs['frequency'] not in s.HISTORY_FREQUENCY:
                return render_template(
                    'error.html', error='Frequency is incorrect'
                )
            try:
                return render_template(**f(*args, **kwargs))
            except ValueError as error:
                return render_template(
                    'error.html', error=error
                )
        return wrapper
    return decorator
