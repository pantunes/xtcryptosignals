__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import pytest
from xtcryptosignals.tasks.utils import (
    get_class,
    convert_to_seconds,
)


def test_get_class():
    with pytest.raises(ModuleNotFoundError):
        get_class('aaa', 'bbb')

    with pytest.raises(ModuleNotFoundError):
        get_class(
            folder='xtcryptosignals.tasks.exchanges',
            module='aaa'
        )

    get_class(
        folder='xtcryptosignals.tasks.exchanges',
        module='binance'
    )


def test_convert_to_seconds():
    with pytest.raises(TypeError):
        convert_to_seconds(5)

    with pytest.raises(TypeError):
        convert_to_seconds(-1)

    with pytest.raises(TypeError):
        convert_to_seconds(None)

    with pytest.raises(ValueError):
        convert_to_seconds('12as')

    assert convert_to_seconds('0s') == 0
    assert convert_to_seconds('5s') == 5
    assert convert_to_seconds('65s') == 65

    assert convert_to_seconds('0m') == 0
    assert convert_to_seconds('10m') == 600
    assert convert_to_seconds('-10m') == -600

    assert convert_to_seconds('0h') == 0
    assert convert_to_seconds('10h') == 36000
    assert convert_to_seconds('-10h') == -36000

    assert convert_to_seconds('0d') == 0
    assert convert_to_seconds('10d') == 864000
    assert convert_to_seconds('-10d') == -864000

    assert convert_to_seconds('0w') == 0
    assert convert_to_seconds('10w') == 6048000
    assert convert_to_seconds('-10w') == -6048000

    assert convert_to_seconds('0y') == 0
    assert convert_to_seconds('10y') == 290304000
    assert convert_to_seconds('-10y') == -290304000
