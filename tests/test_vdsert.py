import pytest
import vdsert

pytest.fixture


def foo():
    return "foo"


def test_all(foo):
    assert vdsert.foo == foo
