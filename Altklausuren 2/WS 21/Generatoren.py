# a)

def my_enumerate(txt):
    for i in range(len(txt)):
        yield (i, txt[i])


# b)

def prefixes(lst):
    yield []
    for i in lst:
        yield lst[:i]


# c)

def alternate(xs, ys):
    for x in xs:
        yield x
        for y in ys:
            yield y


        
if __name__ == '__main__':
    print(list(my_enumerate("abcd")))
    print(list(prefixes([1, 2, 3, 4])))
    print(list(alternate(iter("abcdef"), iter([0, 1, 2]))))