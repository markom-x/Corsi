from seasons import calculate
import pytest, sys

def test_calculate():
    with pytest.raises(SystemExit):
        assert calculate("January 1, 1999") == SystemExit
    assert calculate(
        "2005-07-18") == "Ten million, four hundred fifty-one thousand, five hundred twenty minutes"
