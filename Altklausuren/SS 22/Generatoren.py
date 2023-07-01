from typing import Any

def without(xs: Any, ys: Any):       # if xs not in ys: return xs
    for x in xs:
        if x not in ys:
            yield x


def my_split(text):
    word = ""  # Variable zur Aufnahme der einzelnen Wörter
    if text == '':
        return None
    for char in text:  # Schleife zum Durchlaufen jedes Zeichens im Text
        if char != " ":  # Wenn das Zeichen kein Leerzeichen ist
            word += char  # Füge das Zeichen zum aktuellen Wort hinzu
        elif char == ' ':  # Wenn ein Leerzeichen erreicht wurde und das aktuelle Wort nicht leer ist
            yield word  # Gib das aktuelle Wort mit yield zurück
            word = ""  # Setze das Wort zurück, um das nächste Wort zu sammeln  # Wenn am Ende des Textes noch ein nicht-leeres Wort vorhanden ist
    yield word  # Gib das letzte Wort mit yield zurück






if __name__ == '__main__':
    print(list(without(range(0, 6), [1, 3]))) == [0, 2, 4, 5]

    s1 = 'this is a sentence'
    print(list(my_split(s1)))
    assert list(my_split('')) == []