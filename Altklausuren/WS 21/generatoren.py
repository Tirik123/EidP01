#a)

def my_enumerate(xs):
    i = 0
    for x in xs:
        yield (i, x)
        i += 1


#b)

def prefixes(xs):
    for i in range(len(xs) + 1):
        yield xs[:i]



#c)
def alternate(xs, ys):
    try:
        while True:
            yield next(xs)
            xs, ys = ys, xs
    except:
        yield from ys


if __name__ == '__main__':
    print(list(my_enumerate("abcd")))
    print(list(prefixes([1, 2, 3, 4])))
    print(list(alternate(iter("abcdef"), iter([0, 1, 2]))))