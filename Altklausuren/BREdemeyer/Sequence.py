def count_iterations(n: int) -> int:    # n > 0, return if f == 1
    count = 0
    while n != 1 or count == 0:
        if n % 2 == 0:
            count += 1
            n = n // 2
        elif n % 2 != 0:
            count += 1
            n = 3 * n + 1
    return count


if __name__ == '__main__':
    print(count_iterations(10))
    print(count_iterations(1))