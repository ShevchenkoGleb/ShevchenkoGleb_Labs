import csv

# Укажите имя входного CSV-файла
csv_file_path = 'Список продуктов.csv'

# Инициализация переменной для хранения итоговой суммы
total_sum = 0

# Чтение данных из CSV-файла
with open(csv_file_path, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')  # Указываем разделитель как ';'
    next(reader)# Пропустить заголовок

    print("Нужно купить:")

    for row in reader:#Обработка каждой строки
        product = row[0]
        quantity = int(row[1])
        price = int(row[2])
        total_sum += quantity * price
        print(f"{product} - {quantity} шт. за {price} руб.")
print(f"Итоговая сумма: {total_sum} руб.")
