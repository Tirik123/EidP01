#b)

def dup(n, xs):
    for i in xs:
        for _ in range(n):
            yield i


#c)

def compare(xs, ys):
    yield from map(lambda x, y: max(x, y), xs, ys)



#a)

def my_chain(xs, ys):
    for x in xs:
        yield x
    for y in ys:
        yield y

    
    
if __name__ == '__main__':
    #print(list(dup(3, range(1, 4))))
    print(list(compare(range(6), range(-3, 7, 3))))
    print(list(my_chain(range(5), range(2))))