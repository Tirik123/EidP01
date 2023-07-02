def is_scientific(s: str):
    seperateStrings = s.split("e")

    if "." in seperateStrings[0]:
        splitfirstString = seperateStrings[0].split(".")
        for _ in splitfirstString:
            for j in splitfirstString[0]:
                if j[0] == "-" or "+":
                    for k in j[1:]:
                        if not k.isdigit():
                            return False

    print(seperateStrings)
    if len(seperateStrings) < 2:
        return False

    for x in seperateStrings[0]:
        if x != "+" and x != "-":
            if x.isalpha():
                return False

    for y in seperateStrings[1]:
        if y != "+" and y != "-":
            if y.isalpha():
                return False

    if seperateStrings[1] == "" or seperateStrings[0] == "":
        return False
    for m in seperateStrings[1]:
        if m is None:
            return False
        elif m[0] == "-" or "+":
            for ll in m[1:]:
                if not ll.isdigit():
                    return False
    return True


if __name__ == "__main__":
    print(is_scientific("3.0e5"))
    print(is_scientific("3.0"))
