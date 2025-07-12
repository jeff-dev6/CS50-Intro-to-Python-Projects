from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/4") == 25

def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("abc/2")
    with pytest.raises(ValueError):
        convert("2/abc")
    with pytest.raises(ValueError):
        convert("1/2/3")
    with pytest.raises(ValueError):
        convert("one half")
    with pytest.raises(ValueError):
        convert("5/4")

def test_convert_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(25) == "25%"
    assert gauge(98) == "98%"





