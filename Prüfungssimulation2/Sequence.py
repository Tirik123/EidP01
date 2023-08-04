#a)

def initials(text: str) -> str:
    result = ''
    x = text.split(' ')
    for i in x:
        result += i[0]
    return result


#b)

def balanced_stars(text: str) -> bool:
    result = []
    for i in text:
        if i == '*':
            result.append(i)
    if len(result) % 2 != 0:
        return False
    return True


#c)

def remove_ness(text: str) -> str:
    result = ''
    if text[-4:] == 'ness':
        if text[-5] != 'i':
            result += text[:-4]
        elif text[-5] == 'i':
            result += text[:-5] + 'y'
    elif text[-4:] != 'ness':
        result += text
    return result


#d)




if __name__ == '__main__':
    #print(initials('Hello to the World!'))
    #print(balanced_stars("Hello to* the *World*!"))
    print(remove_ness('goodness'))
    print(remove_ness('happiness'))
    print(remove_ness('cow'))


# 20