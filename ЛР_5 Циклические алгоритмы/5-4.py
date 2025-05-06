import random
count=0
count_correct=0
while count<3:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print(a, '+', b, '=', end=' ')
    otvet = int(input())
    if otvet == a+b:
        count_correct += 1
        print('«Правильно!»')
    else:
        print('«Ответ неверный»')
        count += 1
print('«Игра окончена. Правильных ответов: ',count_correct, '»')

