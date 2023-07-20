def is_url(x: str) -> bool:
    if not x.startswith("http://") and not x.startswith("https://"):
        return False

    elements = x.split("/")[2:]
    domain = elements[0].split('.')
    if len(domain) < 2:
        return False

    for section in domain:
        if not section.isalpha():
            return False

    for pathElement in elements[1:]:
        if not pathElement.isalpha():
            return False
    return True


def test1():
    assert is_url("http") is False


def test2():
    assert is_url("http://uni.") == False


def test3():
    assert is_url("http://uni.freiburg.12") is False


def test4():
    assert is_url("http://uni.1freiburg") is False

if __name__ == '__main__':
    print(test1)
    print(test2)
    print(test3)
    print(test4)