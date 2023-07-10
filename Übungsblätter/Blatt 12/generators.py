from typing import Callable


def differentiate(f: Callable[[float], float], h: float) -> Callable[[float], float]:
    return lambda x: (f(x + h) - f(x - h)) / 2 * h


def newton(f, x):
    yield from x - f(x) / differentiate(f, x)


if __name__ == '__main__':
    generator = newton(lambda x: 2 * x + 1, 3)
    for i in range(3):
        print(next(generator))