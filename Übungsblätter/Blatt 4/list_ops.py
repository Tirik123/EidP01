def reverse(Liste: list) -> list:
    Liste = Liste[::-1]
    return Liste


def only_positive(Liste: list) -> list:
    Positive_Liste =  [i for i in Liste if i > 0]
    return Positive_Liste


def average(Gleitkommazahl_Liste: list) -> float:
    if len(Gleitkommazahl_Liste) == 0:
        return 0.0
    else:
        return sum(Gleitkommazahl_Liste) / len(Gleitkommazahl_Liste) 
    


if __name__ == '__main__':
    assert reverse([]) == []
    assert reverse([1, 2, 3]) == [3, 2, 1]
    assert reverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert only_positive([]) == []
    assert only_positive([1, 2, 3]) == [1, 2, 3]
    assert only_positive([-8, 1, -5, -9, 2, -7, 3, -6, 0]) == [1, 2, 3]
    from math import isclose
    eps = 1e-4
    assert isclose(average([]), 0.0, abs_tol=eps, rel_tol=eps)
    assert isclose(average([1.0]), 1.0, rel_tol=eps)
    assert isclose(average([5.0, 10.0, 15.0, 20.0]), 12.5, rel_tol=eps)
