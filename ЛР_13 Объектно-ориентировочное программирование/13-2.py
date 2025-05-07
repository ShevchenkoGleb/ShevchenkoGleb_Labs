class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name  # Название ресторана
        self.cuisine_type = cuisine_type        # Тип кухни

    def describe_restaurant(self):
        """Выводит информацию о ресторане."""
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        """Выводит сообщение о том, что ресторан открыт."""
        print(f"Ресторан {self.restaurant_name} сейчас открыт!")

# Создание трех разных экземпляров класса Restaurant
restaurant1 = Restaurant("Итальянский вкус", "Итальянская")
restaurant2 = Restaurant("Суши Шоп", "Японская")
restaurant3 = Restaurant("Мексиканская кухня", "Мексиканская")

# Вызов метода describe_restaurant() для каждого экземпляра
restaurant1.describe_restaurant()
print()
restaurant2.describe_restaurant()
print()
restaurant3.describe_restaurant()
