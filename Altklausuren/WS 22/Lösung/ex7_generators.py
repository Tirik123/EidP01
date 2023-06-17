# Aufgabe 7 (Generators) ######################################################

def my_chain(xs, ys):
    yield from xs
    yield from ys


def dup(n, xs):
    for x in xs:
        for _ in range(n):
            yield x


def compare(xs, ys):
    yield from map(max, xs, ys)


def test_ex7_generators():
    assert list(my_chain(range(5), range(2))) == [0, 1, 2, 3, 4, 0, 1]
    assert list(dup(3, range(1, 4))) == [1, 1, 1, 2, 2, 2, 3, 3, 3]
    assert list(compare(range(6), range(-3, 7, 3))) == [0, 1, 3, 6]


if __name__ == "__main__":
    test_ex7_generators()
