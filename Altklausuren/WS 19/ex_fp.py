def compose(f, g):
    return lambda x: f(g(x))


def factor_pairs(n: int):
    return [(x, y) for x in range(0, n + 1) for y in range(0, n + 1) if x * y == n]


if __name__ == '__main__':
    def f(x):
        return x + 1
    def g(x):
        return x * 2
    print(compose(f, g)(5))
    print(factor_pairs(6))