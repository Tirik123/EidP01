#a)

def same(f, g):
    return lambda x: f(x) == g(x)


#b)


def check_fun(f, ps):
    return [(x, f(x), y) for x, y in ps if f(x) != y]


#c)


def combinations2(xs: str, ys: str) -> list[str]:
    return list(map(lambda x, y: x + y, ys, xs))




if __name__ == '__main__':
    #f = same(lambda x: x * 2 + 1, lambda x: x * 3)
    #print(f(2))

    #f = lambda x: x * 2
    #ps = [(1, 2), (2, 40), (3, 60), (4, 8)]
    #print(check_fun(f, ps))
    
    print(combinations2('abc', '12'))



#10.5/15