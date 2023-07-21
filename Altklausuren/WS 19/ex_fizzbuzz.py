def fizzbuzz(n: int) -> str:
    if n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    elif n % 3 == 0 and n % 5 != 0:
        return "fizz"
    elif n % 3 != 0 and n % 5 == 0:
        return "buzz"
    else:
        return str(n)
    

def test_3_and_5():
    assert fizzbuzz(15) == "fizzbuzz"


def test_3_and_not_5():
    assert fizzbuzz(3) == "fizz"


def test_not_3_and_5():
    assert fizzbuzz(5) == "buzz"


def test_else():
    assert fizzbuzz(4) == str(4)


if __name__ == '__main__':
    test_3_and_5()
    test_3_and_not_5()
    test_not_3_and_5()
    test_else()