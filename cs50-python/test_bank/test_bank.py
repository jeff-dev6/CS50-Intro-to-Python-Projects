import pytest

from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("Hello There") == 0

def test_h_but_not_hello():
    assert value("hi") == 20
    assert value("house") == 20
    assert value("Hamathan") == 20

def test_other_items():
    assert value("what's up") == 100
    assert value("python") == 100
