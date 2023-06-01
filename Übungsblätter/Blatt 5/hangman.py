def input_choice(question: str, answer_list: list[str]) -> str:
    answer = input(f'{question}, {answer_list}')
    if answer in answer_list:
        return answer
    else:
        while answer not in answer_list:
            print('Invalid answer. Try again.')
            answer = answer = input(f'{question}, {answer_list}')
            return answer
    return answer
        

def shape(word: str, guesses: str) -> str:
    empty_word = ''
    for i in word:
        if i in guesses:
            empty_word += i  
        else:
            empty_word += '_'
    return empty_word


'''def shape(word: str, guesses: str) -> str:
    s = ''
    for c in word:
        if c in guesses:
            s += c
        else:
            s += '_'
    return s'''


def hangman(word: str, mistakes: int):
    empty_word = ''
    while mistakes != 0:
        answer = input(f'{mistakes} mistakes left; make a guess:')
        print(shape(word, answer))
        empty_word += shape(word, answer)
        if answer not in word:
            mistakes -= 1
            if mistakes == 0 or empty_word == word:
                break
    



if __name__ == '__main__':
    #print(input_choice("Do you want to play a game ?", ['yes', 'no']))
    #print(shape('weather', 'aewhtr'))
    print(hangman('weather', 5))
    