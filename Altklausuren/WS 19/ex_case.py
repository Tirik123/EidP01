def to_snake(s: str) -> str:    #from myFancyFunction to my_fance_function
    new_str = ''
    for i in s:
        if not i.isupper():
            new_str += i
        elif i.isupper():
            i = i.lower()
            new_str += '_'
            new_str += i
    return new_str


def to_camel(s: str) -> str:    # from my_fancy_function to myFancyFunction
    x = s.split("_")
    new_str = ''
    for i in x[0]:
        for k in i:
            new_str += i
    for i in x[1:]:
        for k in i[0]:
            k = k.upper()
            new_str += k
        for p in i[1:]:
            new_str += p
    return new_str


def test_to_snake():
    assert to_snake('myFancyFunction') == "my_fancy_function"


def test_to_camel():
    assert to_camel('my_Fancy_Function') == "myFancyFunction"


if __name__ == '__main__':
    print(to_snake('myFancyFunction'))
    print(to_camel('my_fancy_function'))
    test_to_snake()
    test_to_camel()
