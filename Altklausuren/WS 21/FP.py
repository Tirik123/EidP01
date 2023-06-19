#a)

def twice(f):
    return lambda x: f(f(x))



#b)

def pythagorean_triples(n):
    return [(a,b,c) for a in range(1, n)
                    for b in range(a, n)
                    for c in range(b, n)
                    if a ** 2 + b ** 2 == c ** 2]


if __name__ == '__main__':
    print(twice(lambda x: x*2)(5))
    print(list(pythagorean_triples(15)))
