# z = 0.0 < float < 10.0
# y = beliebige Zahl
# z e y = x * 10 ** y

def is_scientific(s: str) -> bool:
    if 'e' not in s:
        return False
    if '.' not in s:
        return False
    split = s.split('e')
    x = split[0]
    if x[0] == '-' or x[0] == '+':
        if len(x) > 4:
            return False
        if x[1].isdigit() is False:
            return False
        if x[2] != '.':
            return False
        if x[3].isdigit() is False:
            return False
        if x[1].isdigit() is True:
            if int(x[1]) >= 10 and int(x[1]) <= 0:
                return False
    elif x[0] != '-' and x[0] != '+':
        if len(x) > 3 or len(x) < 1:
            return False
        if x[0].isdigit() is False:
            return False
        if x[1].isdigit() is False:
            if x[1] != '.':
                return False
        if x[2].isdigit() is False:
            return False
        if x[0].isdigit() is True:
            if int(x[0]) >= 10 and int(x[0]) <= 0:
                return False
        if x[2].isdigit() is True:
            if int(x[2]) >= 10 and int(x[2]) <= 0:
                return False
    y = split[1]
    if len(y) < 1:
        return False
    if y[0] == '-' or y[0] == '+':
        if y[1:].isdigit() is False:
            return False
    elif y[0] != '-' and y[0] != '+':
        if y[0:].isdigit() is False:
            return False
    return True



if __name__ == '__main__':
    print(is_scientific('3.0e5'))