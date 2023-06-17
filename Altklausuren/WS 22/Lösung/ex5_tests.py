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


# Aufgabe 5 (Tests) ###########################################################

def test_is_strong():
    assert not is_strong("aab")


def test_is_strong2():
    assert not is_strong("aab1")


def test_is_strong3():
    assert not is_strong("aab4567A")


def test_is_strong4():
    assert is_strong("aabAB123C4")


if __name__ == "__main__":
    test_is_strong()
    test_is_strong2()
    test_is_strong3()
    test_is_strong4()
