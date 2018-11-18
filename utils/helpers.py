__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__version__ = "1.0"
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
        return int(x[:-1])
    if _t == 'm':
        return int(x[:-1]) * 60
    # hours
    return int(x[:-1]) * 60 * 60
