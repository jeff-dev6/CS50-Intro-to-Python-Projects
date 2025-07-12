from plates import is_valid


def test_must_start_with_two_letters():
    assert is_valid("BA123") == True
    assert is_valid("234BAT") == False
    assert is_valid("1A") == False
    assert is_valid("5S50") == False
    assert is_valid("A123") == False
    assert is_valid("C2") == False
    assert is_valid("2B") == False
    assert is_valid("AA1234") == True

def test_number_of_char():
    assert is_valid("AA") == True
    assert is_valid("ANSHDB") == True
    assert is_valid("A") == False
    assert is_valid("AAA65784") == False

def test_number_placement():
    assert is_valid("CS05") == False
    assert is_valid("AACG09HG") == False
    assert is_valid("0CSWEE") == False
    assert is_valid("CSNG0") == False
    assert is_valid("HSG01GSH10") == False
    assert is_valid("CS50H") == False

def test_edge_cases():
    assert is_valid(" ") == False
    assert is_valid("") == False
    assert is_valid( "CS 50"  ) == False
    assert is_valid("CS50!AGG") == False

