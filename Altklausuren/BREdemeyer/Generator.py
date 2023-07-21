from typing import Iterator, Optional


def multiples(n: int, max: Optional[int] = None) -> Iterator[int]:
    last = n
    while max is None or last < max:
        yield last
        last += n


#def my_sum(xs: Iterator[int]) -> int:



if __name__ == '__main__':
    it = iter(multiples(7, 51))
    print(list(it))