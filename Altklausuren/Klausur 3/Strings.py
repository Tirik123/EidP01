def is_scientific(s: str) -> bool:
    if 'e' not in s:
        return False
    if s == '':
        return False
    x = s.split('e')
    print(x)
    if len(x) != 2:
        return False
    return True



if __name__ == '__main__':
    print(is_scientific('-3.0175e-5'))
