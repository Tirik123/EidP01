def is_strong(pw: str) -> bool:
    ziffer_list = []
    sonder_list_1 = []
    upper_list = []
    sonder_list_2 = []
    if len(pw) < 8:
        return False
    for digit in pw:
        if digit.isdigit() == True:
            ziffer_list += digit
    if len(ziffer_list) < 1:
        return False
    if len(ziffer_list) < 0 and len(ziffer_list) <= 3:
        for sonder in pw:
            if sonder == '!' or sonder == '?' or sonder == '+' or sonder == '*':
                sonder_list_1 += sonder
        if len(sonder_list_1) < 1:
            return False
        elif len(sonder_list_1) >= 2:
            return True
    for upper in pw:
        if upper.isupper() == True:
            upper_list += upper
    if len(upper_list) < 3:
        for sonder in pw:
            if sonder == '!' or sonder == '?' or sonder == '+' or sonder == '*':
                sonder_list_2 += sonder
        if len(sonder_list_2) < 1:
            return False
        elif len(sonder_list_1) >= 2:
            return True
    return True
    


if __name__ == '__main__':
    print(is_strong('aaaaaaaa1!'))
            

    
    