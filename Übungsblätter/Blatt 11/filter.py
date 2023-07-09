def my_filter(xs, ys):
    return {x for x in xs if x not in ys}


def my_diff(xs, ys):
    return my_filter(xs, ys) | my_filter(ys, xs)

if __name__ == '__main__':
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}
    #assert my_filter(set1, set2) == {1, 2}
    print(my_diff(set1, set2))
