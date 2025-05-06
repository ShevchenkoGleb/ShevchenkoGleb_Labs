countries_and_capitals = {
    "Россия": "Москва",
    "США": "Вашингтон",
    "Франция": "Париж",
    "Германия": "Берлин",
    "Италия": "Рим",
    "Китай": "Пекин",
    "Япония": "Токио",
    "Индия": "Нью-Дели"
}

print("Список стран и их столиц:")
for country, capital in countries_and_capitals.items():
    print(f"{country}: {capital}")

country_to_find = input("Введите страну: ")
capital_of_country = countries_and_capitals.get(country_to_find, "Страна не найдена")
print(f"\nСтолица {country_to_find}: {capital_of_country}")


print("\nСписок стран и их столиц в алфавитном порядке:")
for country in sorted(countries_and_capitals.keys()):
    print(f"{country}: {countries_and_capitals[country]}")
