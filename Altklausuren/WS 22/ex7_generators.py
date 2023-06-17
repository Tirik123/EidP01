# Aufgabe 7 (Generators) ######################################################


# (a) #########################################################################

def my_chain(xs, ys):
    yield from xs
    yield from ys

def my_chain2(xs, ys): # alternativ
    for x in xs:
        yield x
    for y in ys:
        yield y



# (b) #########################################################################

def dup(n: int, xs):
    for x in xs:
        for _ in range(n):
            yield x    




# (c) #########################################################################

def compare(xs, ys):
    yield from map(max, xs, ys)





if __name__ == '__main__':
    print((list((my_chain(range(5), range(2))))))
    print(list(dup(3, range(1, 4))))
    print(list(compare(range(6), range(-3, 7, 3))))