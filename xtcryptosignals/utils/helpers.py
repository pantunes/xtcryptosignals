__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from importlib import import_module


def get_class(folder, module):
    exchange_module = import_module(
        '{}.{}'.format(folder, module)
    )
    return getattr(exchange_module, module.capitalize())


def convert_to_seconds(x):
    _t = x[-1]
    if _t == 's':
        # seconds
        return int(x[:-1])
    if _t == 'm':
        # minutes
        return int(x[:-1]) * 60
    if _t == 'h':
        # hours
        return int(x[:-1]) * 60 * 60
    if _t == 'd':
        # days
        return int(x[:-1]) * 60 * 60 * 24
    if _t == 'w':
        # weeks
        return int(x[:-1]) * 60 * 60 * 24 * 7
    raise ValueError('Undefined item: {}'.format(x))
