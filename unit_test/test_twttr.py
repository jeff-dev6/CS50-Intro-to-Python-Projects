from twttr import shorten


def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("TwItTeR") == "TwtTR"
    assert shorten("aeiouAEIOU") == ""
    assert shorten("Python Programming") == "Pythn Prgrmmng"
    assert shorten("") == ""
