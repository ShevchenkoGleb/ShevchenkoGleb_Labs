words=""
while True:
    word = input("Введите слово (для окончания слов введи 'stop'): ")
    if word == 'stop':
        break
    words += " "
    words += word
print('Получилась строка:', words)