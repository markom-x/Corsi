from plates import is_valid

def test_2letters():
    assert is_valid("CS50") == True
    assert is_valid("C503") == False

def test_6characters():
    assert is_valid("PF104") == True
    assert is_valid("PF104JS") == False
    assert is_valid("P") == False

def test_numbers():
    assert is_valid("CFA402") == True
    assert is_valid("CFA40F") == False
    assert is_valid("CF042") == False

def test_pspm():
    assert is_valid("CS50") == True
    assert is_valid("CS,50.") == False
