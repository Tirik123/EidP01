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


if __name__ == '__main__':
    f = lambda x: x + 1
    g = times_2(f)
    print(g(3))