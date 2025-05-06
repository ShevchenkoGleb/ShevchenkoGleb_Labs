numb=int(input("Введите номер места: "))
if numb % 2 == 0 and numb <= 36:
    print("Верхнее, купе")
elif numb % 2 != 0 and numb <= 36:
    print("Нижнее, купе")
elif numb % 2 == 0 and 54 >= numb > 36:
    print("Нижнее, боковое")
elif numb % 2 != 0 and 54 >= numb > 36:
    print("Верхнее, боковое")
else:
    print("Такого места нет")