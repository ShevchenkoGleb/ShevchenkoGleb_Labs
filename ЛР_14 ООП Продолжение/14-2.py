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
    def __init__(self, restaurant_name, cuisine_type, flavors, location, working_hours, rating=0):
        super().__init__(restaurant_name, cuisine_type, rating)  # Вызов конструктора родительского класса
        self.flavors = flavors  # Список сортов мороженого
        self.location = location  # Локация кафе
        self.working_hours = working_hours  # Время работы кафе

    def display_flavors(self):
        """Выводит список сортов мороженого."""
        print(f"Сорта мороженого в кафе '{self.restaurant_name}':")
        for flavor in self.flavors:
            print(f"- {flavor}")

    def add_flavor(self, flavor):
        """Добавляет новый сорт мороженого."""
        if flavor not in self.flavors:
            self.flavors.append(flavor)
            print(f"Сорт мороженого '{flavor}' добавлен.")
        else:
            print(f"Сорт мороженого '{flavor}' уже существует.")

    def remove_flavor(self, flavor):
        """Удаляет сорт мороженого."""
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Сорт мороженого '{flavor}' удален.")
        else:
            print(f"Сорт мороженого '{flavor}' не найден.")

    def check_flavor(self, flavor):
        """Проверяет наличие сорта мороженого."""
        if flavor in self.flavors:
            print(f"Сорт мороженого '{flavor}' доступен.")
            return True
        else:
            print(f"Сорт мороженого '{flavor}' недоступен.")
            return False

    def display_info(self):
        """Выводит информацию о кафе и его локации и времени работы."""
        self.describe_restaurant()
        print(f"Локация: {self.location}")
        print(f"Время работы: {self.working_hours}")

    def serve_soft_serve(self):
        """Обслуживает мягкое мороженое."""
        print("Обслуживаем мягкое мороженое.")

    def serve_popsicle(self):
        """Обслуживает мороженое на палочке."""
        print("Обслуживаем мороженое на палочке.")

# Создание экземпляра IceCreamStand
ice_cream_stand = IceCreamStand(
    "Сладкий холод",
    "Десерты",
    ["Ваниль", "Шоколад", "Клубника", "Мята"],
    "Центральный парк",
    "10:00 - 20:00",
    4.9
)

# Вызов методов для отображения информации о кафе
ice_cream_stand.display_info()
print()  # Пустая строка для разделения вывода

# Вызов метода display_flavors() для отображения сортов мороженого
ice_cream_stand.display_flavors()
print()  # Пустая строка для разделения вывода

# Добавление и удаление сортов
ice_cream_stand.add_flavor("Карамель")
ice_cream_stand.remove_flavor("Клубника")
ice_cream_stand.check_flavor("Шоколад")
ice_cream_stand.check_flavor("Клубника")
print()  # Пустая строка для разделения вывода

# Обслуживание разных типов мороженого
ice_cream_stand.serve_soft_serve()
ice_cream_stand.serve_popsicle()
