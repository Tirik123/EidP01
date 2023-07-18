def count_iterations(n: int, a: int) -> int:
    iter = 0
    while n < a:
        if n % 2 == 0:
            n = n // 2
            iter += 1
        n = 9 * n + 3
        iter += 1
    return iter

if __name__ == '__main__':
    print(count_iterations(3, 100))





# 10/10