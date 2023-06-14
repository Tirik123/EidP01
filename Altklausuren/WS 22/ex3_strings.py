# Aufgabe 3 (Strings) #########################################################

def is_list_of_int(x: str) -> bool:
    if x[0] != "[" or x[-1] != "]" or len(x) < 2:
        return False
    
    splits = x.split(",")
    #return splits
    for s in splits:
        if s.isdigit() == True and s != int:
            return False
        if not s.isdigit():
            return False 
    return True

        #print(s)








if __name__ == '__main__':
    print(is_list_of_int("[100,-44,0]"))