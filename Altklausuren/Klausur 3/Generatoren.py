def accumulate(xs):
    result = 0
    for x in xs:
        result += x
        yield result


def my_map(f, xs):
    for i in xs:
        yield f(i)


def double(n: int) -> int:
    return n * 2

def init(xs):
    num_elements = 0
    last_element = None

    for item in xs:
        num_elements += 1
        last_element = item

    if num_elements <= 1:
        return

    for _ in range(num_elements - 1):
        yield next(xs)



if __name__ == '__main__':
    print(list(accumulate(iter([1, 2, 3, 4, 5, 6]))))
    print(list(my_map(double, iter([1, 2, 3, 4]))))
    print(list(init(iter([1, 2, 3, 4]))))
    print(list(init(iter([]))))