def alles(xs, n):
    return all(x % n == 0 for x in xs)






a = [1, 2, 3, 4]

print(alles(a, 2))
