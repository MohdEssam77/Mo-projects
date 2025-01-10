from jar import Jar


def test_init():
    jar = Jar()
    assert jar._capacity == 12
    assert jar._size == 0
    newjar = Jar(7)
    assert newjar._capacity == 7
    assert newjar._size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar._size == 2

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(3)
    assert jar._size == 7
