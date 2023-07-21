def dot_product(xs: list[int], ys: list[int]) -> int:
    return sum(map(lambda x, y: x * y, xs, ys))


def matrix_mult(m: list[list[int]], xs: list[int]) -> list[int]:
    return [dot_product(xs, ys) for ys in m]


if __name__ == '__main__':
    xs = [1, 2, 3, 4]
    ys = [40, 30, 20, 10]
    print(dot_product(xs, ys))
    assert dot_product(xs, ys) == 40 * 1 + 30 * 2 + 20 * 3 + 10 * 4