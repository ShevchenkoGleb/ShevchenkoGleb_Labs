color1 = str(input("Введите цвет(красный,синий,жёлтый): "))
color2 = str(input("Введите цвет(красный,синий,жёлтый): "))
if (color1 == 'красный' and color2 == 'синий') or (color2 == 'красный' and color1 == 'синий'):
    print('фиолетовый')
elif (color1 == 'красный' and color2 == 'жёлтый') or (color2 == 'красный' and color1 == 'жёлтый'):
    print('оранжевый')
elif (color1 == 'синий' and color2 == 'жёлтый') or (color2 == 'красный' and color1 == 'жёлтый'):
    print('зелёный')
else:
    print("Ошибка!")