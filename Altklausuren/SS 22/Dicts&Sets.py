def words_by_length(text: str) -> dict[int, set[str]]:
    new_dict = {}
    x = text.split()
    #print(x)
    for length in x:
        if len(length) > 0:
            if len(length) not in new_dict:
                new_dict[len(length)] = {length}
            else:
                new_dict[len(length)].add(length)
    return new_dict
    




if __name__ == '__main__':
    print(words_by_length("das ja genau das will ich"))