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
                ), 404
            try:
                return render_template(**f(*args, **kwargs))
            except ValueError as error:
                return render_template(
                    'error.html', error=error
                ), 404
        return wrapper
    return decorator


def get_pairs():
    pairs = set()
    for i in s.SYMBOLS_PER_EXCHANGE:
        for a, b in i.items():
            for c, d in b['pairs']:
                pairs.add(c + d)
    return ['ALL'] + sorted(pairs)
