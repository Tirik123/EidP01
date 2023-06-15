# Aufgabe 5 (Tests) ###########################################################

def is_strong(pw: str) -> bool:
    int_count = 0
    upper_count = 0
    used_specials = []

    for c in pw:
        if c.isupper():
            upper_count += 1
        elif c.isdigit():
            int_count += 1
        elif not c.islower():
            used_specials += [c]

    if int_count < 1:
        return False
    elif int_count <= 3:
        if len(used_specials) > 0:
            used_specials.pop(0)
        else:
            return False

    if upper_count <= 2:
        if len(used_specials) > 0:
            used_specials.pop(0)
        else:
            return False
    return True


def test1():
    assert is_strong("") == False

def test2():
    assert is_strong("134") == False

def test3():
    assert is_strong("1234") == False

def test4():
    assert is_strong("1234ABC") == True


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()


