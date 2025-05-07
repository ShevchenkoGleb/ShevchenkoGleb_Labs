class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name  # Название ресторана
        self.cuisine_type = cuisine_type        # Тип кухни
        self.rating = rating                    # Рейтинг ресторана (по умолчанию 0)

    def describe_restaurant(self):
        """Выводит информацию о ресторане."""
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")

    def open_restaurant(self):
        """Выводит сообщение о том, что ресторан открыт."""
        print(f"Ресторан {self.restaurant_name} сейчас открыт!")

    def update_rating(self, new_rating):
        """Обновляет рейтинг ресторана."""
        self.rating = new_rating
        print(f"Рейтинг ресторана {self.restaurant_name} обновлен на {self.rating}")

# Создание трех разных экземпляров класса Restaurant
restaurant1 = Restaurant("Итальянский вкус", "Итальянская", 4.5)
restaurant2 = Restaurant("Суши Шоп", "Японская", 4.8)
restaurant3 = Restaurant("Мексиканская кухня", "Мексиканская", 4.2)

# Вызов метода describe_restaurant() для каждого экземпляра
restaurant1.describe_restaurant()
print()
restaurant2.describe_restaurant()
print()
restaurant3.describe_restaurant()
print()

# Обновление рейтинга для одного из ресторанов
restaurant1.update_rating(4.7)
restaurant1.describe_restaurant()  # Проверка обновленного рейтинга
