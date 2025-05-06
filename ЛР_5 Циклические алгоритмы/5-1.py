N=int(input("Введите кол-во слов: "))
n=0
words=""
while n < N:
    word = input("Введите слово: ")
    words += " "
    words += word
    n = n + 1
print('Получилась строка:', words)