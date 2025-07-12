from working import convert
import pytest

def test_full_time():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("3:30 PM to 4:30 AM") == "15:30 to 04:30"

def test_short_time():
    assert convert("5 PM to 4 AM") == "17:00 to 04:00"
    assert convert("12 PM to 3 AM") == "12:00 to 03:00"
    assert convert("12 AM to 9 PM") == "00:00 to 21:00"

def test_mixed_time():
    assert convert("4:40 AM to 2 PM") == "04:40 to 14:00"

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("6 AM to 17:00 PM")
    with pytest.raises(ValueError):
        convert("6AM-3PM")
    with pytest.raises(ValueError):
        convert("")
    with pytest.raises(ValueError):
        convert("6:00 AM  5:00 PM")
    with pytest.raises(ValueError):
        convert("5 PM to 3:00")

def test_invalid_time():
    with pytest.raises(ValueError):
        convert("13:00 AM to 9:00 PM")
    with pytest.raises(ValueError):
        convert("7:65 AM to 1 PM")
    with pytest.raises(ValueError):
        convert("7 AM to 1:78 PM")


