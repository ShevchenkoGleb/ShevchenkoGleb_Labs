'''def rare_words():
    """
    Функция проверки и вывода редкости слов
    """
    while True:
        word = input("Введите слово: ").lower()
        if word == 'stop':
            break
        if 'ф' in word:
            print("Ого! Это редкое слово!")
        else:
            print("Эх, это не очень редкое слово...")


if __name__ == '__main__':
    rare_words()'''

n=0
while True:
    word = str(input("Введите слово (для окончания слов введи 'stop'): "))
    if word == 'stop':
        break

    for x in word:
        if x == 'ф':
            n=n+1
            if n>0:
                print("Ого! Это редкое слово!")
            break
    else:
        print("Эх, это не очень редкое слово...")
