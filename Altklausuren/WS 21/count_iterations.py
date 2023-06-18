def count_iterations(n: int) -> int:
    iter = 0
    while n != 0:
        if n % 3 == 0:
            n += 4
            iter += 1
        elif n % 3 != 0 and n % 4 == 0:
            n = n // 2
            iter += 1
        elif n % 3 != 0 and n % 4 != 0:
            n -= 1
            iter += 1
    return iter


if __name__ == '__main__':
    print(count_iterations(5))