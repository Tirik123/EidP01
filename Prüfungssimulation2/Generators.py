from typing import Iterable, Iterator

#a)

def without(xs: Iterable, ys: list) -> Iterator:
    for x in xs:
        if x not in ys:
            yield x


#b)

def my_split(text: str) -> Iterator[str]:
    for i in text:
        if i.isalpha() == False:
            yield text


if __name__ == '__main__':
    assert list(without(range(0, 6), [])) == [0, 1, 2, 3, 4, 5]
    assert list(without(range(0, 6), [1, 3])) == [0, 2, 4, 5]

    assert list(my_split('')) == []
    s1 = 'this is a sentence'
    #assert list(my_split(s1)) == ['this', 'is', 'a', 'sentence']
    print(list(my_split(s1)))


#7/15