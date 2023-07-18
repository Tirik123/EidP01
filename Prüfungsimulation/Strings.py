def is_list_of_int(x: str) -> bool:
    if x is None:
        return False
    if x[0] == "[" and x[-1] == "]":
        if " " not in x:
            return True
    return False

if __name__ == '__main__':
    print(is_list_of_int("[100,-44,0]"))
    print(is_list_of_int("[123,456,]"))




# 10/20
        