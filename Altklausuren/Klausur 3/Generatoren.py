def accumulate(xs):
    for x in xs:
        for y in xs:
            yield x + y


def my_map(f, xs):
    for i in xs:
        yield f(i)


def double(n: int) -> int:
    return n * 2


def init(xs):
    if xs == []:
        return []
    for i in xs:
        yield i - 1


if __name__ == '__main__':
    print(list(accumulate(iter([1, 2, 3, 4, 5, 6]))))
    print(list(my_map(double, iter([1, 2, 3, 4]))))
    print(list(init(iter([1, 2, 3, 4]))))
    print(list(init(iter([]))))