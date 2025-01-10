from working import convert
import pytest

def main():
    test_WrongFormat()
    test_WrongH()
    test_WrongM()
    test_time()


def test_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("11 PM to 6 AM") == "23:00 to 06:00"
    assert convert("5:30 PM to 6:30 AM") == "17:30 to 06:30"


def test_WrongFormat():
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")

def test_WrongH():
    with pytest.raises(ValueError):
        convert("13 PM to 17 PM")

def test_WrongM():
    with pytest.raises(ValueError):
        convert("9:60 AM to 9:60 PM")



if __name__ == "__main__":
    main()
