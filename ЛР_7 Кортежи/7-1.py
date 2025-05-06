import random
spisok=[random.randint(1, 50) for i in range(5)]
print(spisok)
a=int(input("Введите число: "))
if a in spisok:
    print(f"Список: {spisok}, Ваше число: {a}")
    print("Поздравляю, Вы угадали число!")
else:
    print("Нет такого числа!")