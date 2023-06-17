# Aufgabe 8 (Funktionale Programmierung) ######################################

# (a) #########################################################################

def times_2(f):
    return lambda x: f(x) * 2


# (b) #########################################################################

def map_matrix(f, m):
    return [[f(x) for x in row] for row in m]


# (c) #########################################################################

def map_matrix_2(f, m):
    return list(map(lambda row: list(map(f, row)), m))


if __name__ == "__main__":
    m1 = [[1, 2, 3],
          [4, 5, 6]]
    m2 = [[2,  4,  6],
          [8, 10, 12]]

    assert map_matrix(lambda x: x * 2, m1) == m2
    assert map_matrix_2(lambda x: x * 2, m1) == m2
