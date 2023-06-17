# Aufgabe 1 (Sequence) ########################################################

def count_iterations(n: int, a: int) -> int:
    i = 0
    while n <= a:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 9 * n + 3
        i += 1
    return i


def test_ex1_sequence():
    assert count_iterations(101, 100) == 0
    assert count_iterations(3, 100) == 3
    assert count_iterations(32, 1300) == 20


if __name__ == "__main__":
    test_ex1_sequence()
