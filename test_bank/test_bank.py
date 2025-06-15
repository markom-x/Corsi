from bank import value

def test_core():
    assert value("hello") == 0
    assert value("Hi") == 20
    assert value("Bye") == 100

def test_numbers():
    assert value("4") == 100

def test_casefold():
    assert value("HeLLo") == 0
    assert value("handm") == 20
