from project.project import greeting, byebye, game_validation

def main():
    test_greeting()
    test_byebye()
    test_game_validation()

def test_greeting():
    assert greeting("english") == "HELLO!"
    assert greeting("german") == "HALLO!"


def test_byebye():
    assert byebye("english") == "BYE!"
    assert byebye("spanish") == "ADIOS!"


def test_game_validation():
    assert game_validation(3) == 3
    assert game_validation(7) == 7


if __name__ == "__main__":
    main()
