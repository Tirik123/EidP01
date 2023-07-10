from typing import Callable
import math

#a)
def differentiate(f: Callable[[float], float], h: float) -> Callable[[float], float]:
    return lambda x: (f(x + h) - f(x - h)) / 2 * h



#b)
'''def integrate(f: Callable[[float], float], n: int) -> Callable[[float, float], float]:
    h = lambda b, a: (b - a) / n
    x = lambda a, i, h: a + i * h
    s = lambda h: h / 6 * (lambda x: f(x) + 4 * f((x + x) / 2) + f(x))
    for i in range(0, n - 1):
        s = sum(i)
    return s'''




if __name__ == '__main__':
    #print(differentiate(lambda x: 1 / 2 * x ** 2, 1e-2)(0))
    #print(integrate(lambda x: math.exp(x), 5)(0, 1))