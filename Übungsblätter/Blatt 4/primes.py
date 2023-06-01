def is_prime(x: int, ps: list[int]) -> bool:
    for i in ps:
        if x % i != 0:
            return True
    return False



def primes(x: int) -> list[int]:
    prime_list = []
    x_list = list(range(2, x + 1))
    if x >= 2:
        prime_list.append(2)
    else:
        return []
    for i in x_list:
        if i % 2 != 0:
            prime_list.append(i)
    if is_prime(x, prime_list) == True:
        return sorted(prime_list)
    return sorted(prime_list)



if __name__ == '__main__':
    #print(is_prime(17, [2]))
    print(primes(20))
    assert primes(1) == []
    assert primes(3) == [2, 3]
    assert primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]