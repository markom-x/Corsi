from numb3rs import validate

def test_validate():
    assert validate("255.32.23.2") == True
    assert validate("256.21.13.4") == False
    assert validate("255.342.234.4") == False
    assert validate("cat") == False
