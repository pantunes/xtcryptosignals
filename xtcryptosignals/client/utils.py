__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from functools import wraps
from flask import render_template, g


def validate_args():
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if kwargs['frequency'] not in g.HISTORY_FREQUENCY:
                return render_template(
                    'error.html', error='Frequency is incorrect'
                ), 404
            try:
                return render_template(**f(*args, **kwargs))
            except ValueError as error:
                return render_template(
                    'error.html', error=error
                ), 404
        return wrapper
    return decorator

