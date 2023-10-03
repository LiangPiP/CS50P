from plates import is_valid

def test_toolittle():
    assert is_valid("a")==False

def test_toomuch():
    assert is_valid("snkqweu")==False

def test_nummid():
    assert is_valid("AAA22A")==False
    assert is_valid("AAA222")==True

def test_marks():
    assert is_valid('AAs,')==False

def test_alphbegin():
    assert is_valid('A1')==False

def test_zerobegin():
    assert is_valid('AA01')==False