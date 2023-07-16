#a)

def my_chain(xs, ys):
    for x in xs:
        yield x
    for y in ys:
        yield y


#b)

def dup(n, xs):
    pass



#c)

def compare(xs, ys):
    yield from (map(lambda x, y: max(x, y), xs, ys))



if __name__ == '__main__':
    print(list(my_chain(range(5), range(2))))
    #print(list(dup(3, range(1, 4))))
    print(list(compare(range(6), range(-3, 7, 3))))
