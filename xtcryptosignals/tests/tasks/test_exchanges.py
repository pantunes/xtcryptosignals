__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import os
from xtcryptosignals.tasks.utils import get_class


ROOT_FOLDER = os.path.dirname(os.path.abspath(__file__))


def test_exchanges():
    files = os.listdir(
        os.path.join(ROOT_FOLDER, '../../', 'tasks', 'exchanges')
    )
    for filename in files:
        if filename[0] == '_':
            continue
        _class = get_class(
            folder='xtcryptosignals.tasks.exchanges',
            module=filename.partition('.')[0],
        )
        assert _class.get_ticker
