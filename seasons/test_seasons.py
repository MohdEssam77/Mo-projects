from seasons import calculate

def main():
    test_calculate()


def test_calculate():
    assert calculate(2006, 5, 17) == "Nine million, four hundred twenty-four thousand, eight hundred minutes"


if __name__ == "__main__":
    main()
