from um import count

def test_basic():
    assert count("hello, um world") == 1

def test_multiple():
    assert count("um, um, um") == 3

def test_embedded_in_words():
    assert count("Hold an umbrella for your plumbering job today") == 0

def test_no_word():
    assert count("Hello, World") == 0

def test_punctuation():
    assert count("um... his name is um! Jolene") == 2

def test_case_insensitive():
    assert count("Um, UM, uM")  == 3
