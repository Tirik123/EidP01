def leapyear(year: int):
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
    assert leapyear(3) == False



if __name__ == '__main__':
    print(leapyear(4))
    print(leapyear(400))
    print(leapyear(200))
    print(leapyear(3))


#5/5