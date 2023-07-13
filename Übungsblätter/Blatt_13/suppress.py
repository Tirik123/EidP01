from functools import partial
from typing import Callable



def suppress(f: Callable, ignore: tuple):
    def Error_True():
        try:
            return f()
        except ignore:
            return None
    return Error_True




if __name__ == '__main__':
    def foo(n: int) -> int:
        return 35 // n

    assert suppress(partial(foo, 1), ())() == 35 == foo(1)
    #assert suppress(partial(foo, 0), (ZeroDivisionError,))()