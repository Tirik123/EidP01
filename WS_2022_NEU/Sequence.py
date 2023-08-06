def count_iterations(n: int, a: int) -> int:
    result = 0
    while n < a:
        if n % 2 == 0:
            n = n // 2
            result += 1
        n = 9 * n + 3
        result += 1
    return result


if __name__ == '__main__':
    print(count_iterations(3, 100))