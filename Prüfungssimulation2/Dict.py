def words_by_length(text: str) -> dict[int, set[str]]:
    result = {}
    x = text.split(' ')
    for i in x:
        if len(i) not in result:
            result[len(i)] = {i}
        elif len(i) in result:
            result[len(i)].add(i)
    return result


if __name__ == '__main__':
    print(words_by_length("das ja genau das will ich"))


# 5/10