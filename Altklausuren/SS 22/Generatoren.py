from typing import Any

def without(xs: Any, ys: Any):       # if xs not in ys: return xs
    for x in xs:
        if x not in ys:
            yield x



if __name__ == '__main__':
    print(list(without(range(0, 6), [1, 3]))) == [0, 2, 4, 5]