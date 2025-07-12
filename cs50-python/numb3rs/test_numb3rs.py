from numb3rs import validate
import pytest

def test_valid_ips():
    assert validate("1.2.3.4") == True
    assert validate("0.0.0.0") == True
    assert validate("245.20.7.1") == True
    assert validate("255.255.255.255") == True
    assert validate("100.164.200.6") == True

def test_invalid_ips_range():
    assert validate("01.275.30.40") == False
    assert validate("20.59.256.10") == False
    assert validate("300.300.300.300") == False

def test_invalid_ips_format():
    assert validate("20.77.120") == False
    assert validate("250.14.0.1.34") == False

def test_invalid_characters():
    assert validate("cat") == False
    assert validate("10.70.a.50") == False
    assert validate("a.af.hello.world") == False
    assert validate(" ") == False
    assert validate("") == False
    assert validate("...") == False
    assert validate("150.220.1h.50") == False





