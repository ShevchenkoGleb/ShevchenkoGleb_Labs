def delenie_na_3(a):
    if a % 3 == 0:
        return True
    else:
        return False

num = int(input("Введите число: "))
if delenie_na_3(num) == True:
    print(f"{num} делится на 3.")
else:
    print(f"{num} не делится на 3.")

'''def delenie(number):
    if number%3==0:
        print(f"{number} делится на 3.")
    else:
        print(f"{number} не делится на 3.")
delenie(2)'''