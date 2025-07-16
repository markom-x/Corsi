from um import count

def test_count():
    assert count("yummy") == 0
    assert count("hello, um, world") == 1
    assert count("yummy hey um um ciao um") == 3
    assert count("yummy hey UM Um ciao um") == 3
