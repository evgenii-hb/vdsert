import pytest

import vdsert


@pytest.fixture
def foo():
    return "bar"


def test_all(foo):
    assert vdsert.foo() == foo
