def delenie():
    try:
        vvod=input("Введите число: ")
        number=float(vvod)
        res=100/number
        print(f"100 / {number} = {res}")
    except ValueError:
        print("Ошибка: введено не число. Пожалуйста, введите корректное число.")
    except ZeroDivisionError:
        print("Ошибка: делить на 0 нельзя!")
delenie()

