def count_iterations(n: int) -> int:
    count = 0
    while n != 0:
        if n % 3 == 0:
            n += 4
            count += 1
        elif n % 3 != 0 and n % 4 == 0:
            n = n // 2
            count += 1
        elif n % 3 != 0 and n % 3 != 0:
            n -= 1
            count += 1
    return count


if __name__ == '__main__':
    print(count_iterations(5))