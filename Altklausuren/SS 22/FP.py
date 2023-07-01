def same(f, g):
    return lambda x: f(x) == g(x)



def check_fun(f, ps: list[(tuple)]) -> list:
    return [(x, f(x), y) for x, y in ps if f(x) != y]


def combinations2(xs: str, ys: str):
    return list(map(lambda x: list(map(lambda y: x + y, ys)), xs))



def combinations(xs: str, ys: str):
    return [[x + y for y in ys] for x in xs]



if __name__ == '__main__':
    f = same(lambda x: x * 2 + 1, lambda x: x * 3)
    print(f(0))
    print(f(1))
    print(f(2))

    f = lambda x: x * 2
    ps = [(1, 2), (2, 40), (3, 60), (4, 8)]
    print(check_fun(f, ps))

    print(combinations2('abc', '12'))