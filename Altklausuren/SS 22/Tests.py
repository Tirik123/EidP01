def leapyear(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        elif year % 100 == 0 and year % 400 == 0:
            return True
        else:
            return False
    else:
        return False
    

def test1():
    assert leapyear(4) == True

def test2():
    assert leapyear(400) == True

def test3():
    assert leapyear(200) == False

def test4():
    assert leapyear(5) == False


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()