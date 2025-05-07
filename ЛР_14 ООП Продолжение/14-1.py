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


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors, rating=0):
        super().__init__(restaurant_name, cuisine_type, rating)  # Вызов конструктора родительского класса
        self.flavors = flavors  # Список сортов мороженого

    def display_flavors(self):
        """Выводит список сортов мороженого."""
        print(f"Сорта мороженого в кафе '{self.restaurant_name}':")
        for flavor in self.flavors:
            print(f"- {flavor}")


# Создание экземпляра IceCreamStand
ice_cream_stand = IceCreamStand("Сладкий холод", "Десерты", ["Ваниль", "Шоколад", "Клубника", "Мята"], 4.9)

# Вызов метода describe_restaurant() для отображения информации о кафе
ice_cream_stand.describe_restaurant()
print()  # Пустая строка для разделения вывода

# Вызов метода display_flavors() для отображения сортов мороженого
ice_cream_stand.display_flavors()
