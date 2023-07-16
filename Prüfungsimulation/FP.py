#a)

def times_2(f):
    return lambda g: f(g) * 2



#b)

def map_matrix(f, m):
    return [f(m) for x in m]




#c)

def map_matrix_2(f, m):
    return map(lambda x: f(x), m)




if __name__ == '__main__':
    f = lambda x: x + 1
    g = times_2(f)
    print(g(3))
    example = [ [ 1, 2, 3 ]
                , [ 4, 5, 6 ] ]
    print(map_matrix(lambda x: x * 2, example))
    print(map_matrix_2(lambda x: x * 2, example))