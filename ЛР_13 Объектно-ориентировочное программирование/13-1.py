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

# Создание экземпляра класса Restaurant
newRestaurant = Restaurant("Итальянский вкус", "Итальянская")

# Вывод атрибутов
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)

# Вызов методов
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()
