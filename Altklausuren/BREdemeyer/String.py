def is_variable_identifier(x: str, keywords: set[str]) -> bool:
    if len(x) < 1 or len(x) > 64:
        return False
    if x in keywords:
        return False
    for p in x:
        if p.lower():
            continue
        if p.isupper():
            continue
        if p.isdigit():
            continue
        if p == "_":
            continue
        return False
    if x[0].isdigit():
        return False
    return True


if __name__  == '__main__':
    keywords = {"if", "else", "for", "while"}
    print(is_variable_identifier("my_variable", keywords))
    print(is_variable_identifier("0_my_variable", keywords))
    print( is_variable_identifier("for", keywords))

