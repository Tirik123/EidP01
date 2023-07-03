def paired(f, g):
    return lambda x, y: (f(x), g(y))


'''def is_prime(n: int) -> bool:
    return n > 1 and not any(n % i == 0 for i in range(2, int(n ** 0.5) + 1))
'''

def is_prime(n: int) -> bool:
    return n > 1 and not any(n % i == 0 for i in range(2, n))



if __name__ == '__main__':
    result = paired(lambda x: x * 2, lambda x: x * 3)(5, 10)
    print(result)
    print(is_prime(0), is_prime(4), is_prime(5), is_prime(13))
