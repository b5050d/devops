import pytest

from simple_code import add, divide, multiply, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 4) == -4
    assert subtract(-2, -2) == 0


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 10) == 0


def test_divide():
    assert divide(6, 3) == 2
    assert divide(-8, 2) == -4
    with pytest.raises(ValueError):
        divide(5, 0)
