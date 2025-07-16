import pytest
from UnitTests import square

def main():
    test_str()

def test_str():
    with pytest.raises(TypeError):
        square("cat")

if __name__ == "__main__":
    main()
