def word_counts(s: str) -> dict[str, int]:
    result = {}
    x = s.split(' ')
    for i in x:
        if i not in result:
            result[i] = 1
        elif i in result:
            result[i] += 1
    return result


def test_word_counts():
    assert word_counts("This sentence is a sentence") == {'This': 1, 'sentence': 2, 'is': 1, 'a': 1}


if __name__ == '__main__':
    test_word_counts()