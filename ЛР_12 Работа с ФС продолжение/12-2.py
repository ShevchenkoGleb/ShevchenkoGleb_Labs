import json
import os

def load_data(filename): # Функция для сбора данных из файла
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    return {"products": []}

def save_data(filename, data): # Функция для сохранения данных в файл
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def add_product(data): #функция для добавления нового продукта
    name = input("Введите название продукта: ")
    price = float(input("Введите цену продукта: "))
    weight = float(input("Введите вес продукта: "))
    available = input("Продукт доступен? (да/нет): ").strip().lower() == 'да'

    new_product = {
        "name": name,
        "price": price,
        "weight": weight,
        "available": available
    }

    data['products'].append(new_product)

filename = 'products.json'
data = load_data(filename)

add_product(data) #Добавление нового продукта

save_data(filename, data) #Сохранение обновленных данных


print("Содержимое файла products.json:")#Вывод в Python
for product in data['products']:
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    if product['available']:
        print("В наличии")
    else:
        print("Нет в наличии!")
    print()
