from twttr import shorten

def test_case():
    assert shorten("FancUlo") == "Fncl"
    assert shorten("pEPpA") == "pPp"
    assert shorten("pEP,pA") == "pP,p"
    assert shorten("pE2P,pA") == "p2P,p"

