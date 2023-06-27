def initials(text: str) -> str:
    x = text.split()
    initials_list = []
    print(x)
    for word in x:
        initials_list.append(word[0])
    initials_str = "".join(initials_list)
    return initials_str





def balanced_stars(text: str) -> bool:
    star_list = []
    for star in text:
        if star == '*':
            star_list.append(star)
    if len(star_list) % 2 == 0:
        return True
    return False



def remove_ness(text: str) -> str:
    str_y = ""
    for _ in text:
        if text[-4:] == 'ness':
            if text[-5] == 'i':
                str_y += text[0:4]
                str_y += 'y'
                return str_y
            return text[0:4]
    return text
    

def is_bracket_correct(bracket: str) -> bool:
    toClose = []
    for i in bracket:
        if i == "(":
            toClose.append(i)
        elif i == "{":
            toClose.append(i)

    for j in bracket:
        if j == ")":
            if "(" in toClose:
                toClose.remove("(")
        elif j == "}":
            if "{" in toClose:
                toClose.remove("{")

    if len(toClose) != 0:
        return False
    return True




if __name__ == '__main__':
    #print(initials("Hello to the World!"))
    #print(balanced_stars('Hello to *the *World*!'))
    #print(remove_ness("goodness"))
    #print(remove_ness("happiness"))
    #print(remove_ness("cow"))
    print(is_bracket_correct('abc(x)(y)'))

# if 'ness' end text: remove 'ness'
# if 'ness' not end text: return text