import urllib.request

import pytest
import jaraco.functools
from jaraco.context import ExceptionTrap


@jaraco.functools.once
def has_internet():
    with ExceptionTrap() as trap:
        urllib.request.urlopen('http://pypi.org')
    return not trap


def check_internet():
    has_internet() or pytest.skip('Internet connectivity unavailable')


@pytest.fixture
def needs_internet():
    check_internet()
