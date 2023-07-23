def accumulate(xs):
    count = 0
    for x in xs:
        count += x
        yield count


def char_range(start: str, end: str):
    for i in range(ord(start), ord(end) + 1):
        yield chr(i)


def partitions(xs):
    for x in range(len(xs)):
        yield (x + 1, xs[0:x] + xs[x + 1:]) 





if __name__ == '__main__':
    '''print(list(accumulate([1, 2, 3, 4])))
    print(ord("a"))
    print(chr(97))
    print(list(char_range('d', 'h')))'''
    print(list(partitions([1,2,3,4])))