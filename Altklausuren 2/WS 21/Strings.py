def is_strong(pw: str) -> bool:
    zahlen = []
    sonderzeichen_list = []
    groß_list = []
    sonderzeichen = ['!', '?', '+', '*']
    for sonder in pw:
        if sonder in sonderzeichen:
            sonderzeichen_list.append(sonder)
    for groß in pw:
        if groß.isupper() is True:
            groß_list.append(groß)
    for zahl in pw:
        if zahl.isdigit() is True:
            zahlen.append(zahl)
    if len(pw) < 8:
        return False
    if len(zahlen) < 1:
        return False
    if len(zahlen) <= 3:
        if len(sonderzeichen_list) < 1:
            return False
    if len(groß_list) < 3:
        if len(sonderzeichen_list) < 1:
            return False
    if len(zahlen) <= 3 and len(groß_list) < 3:
        if len(sonderzeichen_list) < 2:
            return False
    print(zahlen)
    print(sonderzeichen_list)
    print(groß_list)
    return True



if __name__ == '__main__':
    assert is_strong('') == False
    assert is_strong('1') == False
    assert is_strong('abcdefg1') == False
    assert is_strong('abcdefg1!') == False
    assert is_strong('abcdefg1!A') == False
    assert is_strong('abcdefg1?A?') == True
    print(is_strong('abcdefg1!A'))

