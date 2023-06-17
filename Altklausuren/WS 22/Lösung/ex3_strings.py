# Aufgabe 3 (Strings) #########################################################

def is_list_of_int(x: str) -> bool:
    if len(x) < 2 or x[0] != "[" or x[-1] != "]":
        return False
    x = x[1:-1]

    splits = x.split(",")
    for s in splits:
        if len(s) == 0:
            return False
        if s[0] == "-":
            s = s[1:]
        if not s.isdigit():
            return False
    return True


def test_ex3_strings():
    # ---------- Positive examples

    assert is_list_of_int("[12]")
    assert is_list_of_int("[-12]")
    assert is_list_of_int("[12,-334,34]")
    assert is_list_of_int("[0,0,0]")
    assert is_list_of_int("[0]")

    # Accept leading zeros
    assert is_list_of_int("[-05,05,0,00]")

    # ---------- Negative examples

    # At least one number
    assert not is_list_of_int("[]")

    # Saveguarded against too short strings
    assert not is_list_of_int("[")
    assert not is_list_of_int("]")
    assert not is_list_of_int("")

    # Correct brackets
    assert not is_list_of_int("12,334,434")
    assert not is_list_of_int("[12,334,434")
    assert not is_list_of_int("12,334,434]")
    assert not is_list_of_int("12")

    # Correct numbers
    assert not is_list_of_int("[12,33  4,34]")
    assert not is_list_of_int("[12,33ef4,34]")
    assert not is_list_of_int("[12,33.4,34]")

    # Must not contain spaces
    assert not is_list_of_int("  [12,-334,34]")
    assert not is_list_of_int("[12,-334,34]  ")
    assert not is_list_of_int("[12,  -334,34]")
    assert not is_list_of_int("[12,  -334  ,34]")

    # No multiple minus
    assert not is_list_of_int("[12,--334,34]")
    assert not is_list_of_int("[12,---334,34]")

    # No minus only
    assert not is_list_of_int("[-,334,34]")

    # No plus
    assert not is_list_of_int("[+12,334,34]")
    assert not is_list_of_int("[+,334,34]")
    assert not is_list_of_int("[12,++334,34]")
    assert not is_list_of_int("[12,334+,34]")

    # No minus inside numbers
    assert not is_list_of_int("[12,34-334,34]")
    assert not is_list_of_int("[12,34--334,34]")


if __name__ == "__main__":
    test_ex3_strings()
