def is_list_of_int(x: str):
    lst_num = []
    if x is None:
        return False
    if x[0] != '[' and x[-1] != ']':
        return False
    x = x[1:-1]
    a = x.split(',')
    for i in a:
        if i[0] == '-':
            if i[1:].isdigit() is not True:
                return False
        elif not i.isdigit():
            return False
        elif i.isdigit() is True:
            lst_num.append(i)
    if len(lst_num) < 1:
        return False
    return True
    

if __name__ == '__main__':
    print(is_list_of_int("[100,-44,0]"))
    #print(is_list_of_int("[123,456,]"))
    



    