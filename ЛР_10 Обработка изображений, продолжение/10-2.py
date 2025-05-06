from PIL import Image
check_list={"День Рождения":"birthday.png",
            "Новый Год": "new_year.png",
            "День Победы": "victory_day.png",
            "8 Марта" : "8_marta.png",
            "День Пива": "beer_day.png"}
holiday=input("К какому празднику вам нужна открытка?: ")

if holiday in check_list:
    image = check_list[holiday]
    print(f"Открытка к празднику '{holiday}'")

    try:
        img = Image.open(image)
        img.show()
    except FileNotFoundError:
        print(f"Файл '{image}' не найден.")
else:
    print(f"Открытка к празднику '{holiday}' не найдена.")