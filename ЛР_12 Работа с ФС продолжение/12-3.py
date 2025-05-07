def create_ru_en_dictionary(input_file, output_file):
    ru_en_dict = {}

    # Чтение данных из файла en-ru.txt
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            if ' - ' in line:
                english, russian = line.strip().split(' - ')
                russian_terms = russian.split(', ')

                for term in russian_terms:
                    term = term.strip()  # Убираем лишние пробелы
                    if term not in ru_en_dict:
                        ru_en_dict[term] = []
                    ru_en_dict[term].append(english)

    # Подготовка данных для записи в файл
    sorted_ru_en_list = sorted(ru_en_dict.items())

    # Запись данных в файл ru-en.txt
    with open(output_file, 'w', encoding='utf-8') as file:
        for russian_word, english_words in sorted_ru_en_list:
            file.write(f"{russian_word} – {', '.join(english_words)}\n")

input_file = 'en-ru.txt'
output_file = 'ru-en.txt'

# Создание русско-английского словаря
create_ru_en_dictionary(input_file, output_file)

print(f"Русско-английский словарь успешно создан в файле {output_file}.")
