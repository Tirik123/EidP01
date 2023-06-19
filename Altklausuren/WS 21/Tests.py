import math

def is_prime(n: int) -> bool:
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    else:
        x = math.floor(math.sqrt(n)) + 1
        i = 3
        while i < x:
            if n % i == 0:
                return False
            i += 2
        return True
    


def test1():
    assert is_prime(2) == True

def test2():
    assert is_prime(1) == False

def test3():
    assert is_prime(9) == False

def test4():
    assert is_prime(5) == True


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()

