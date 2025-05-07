import tkinter as tk
from tkinter import messagebox

class IceCreamStand:
    def __init__(self, restaurant_name, cuisine_type, flavors):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.flavors = flavors

    def add_flavor(self, flavor):
        if flavor not in self.flavors:
            self.flavors.append(flavor)
            return True
        return False

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            return True
        return False

    def get_flavors(self):
        return self.flavors

class IceCreamApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ice Cream Stand")

        self.stand = IceCreamStand("Сладкий холод", "Десерты", ["Ваниль", "Шоколад", "Клубника"])

        # Label for current flavors
        self.label = tk.Label(root, text="Доступные сорта мороженого:")
        self.label.pack()

        # Listbox to display flavors
        self.flavor_listbox = tk.Listbox(root)
        self.flavor_listbox.pack()

        # Button to refresh the flavor list
        self.refresh_button = tk.Button(root, text="Обновить список", command=self.refresh_flavors)
        self.refresh_button.pack()

        # Entry for adding new flavors
        self.new_flavor_entry = tk.Entry(root)
        self.new_flavor_entry.pack()
        self.new_flavor_entry.insert(0, "Введите новый сорт")

        # Button to add new flavor
        self.add_flavor_button = tk.Button(root, text="Добавить сорт", command=self.add_flavor)
        self.add_flavor_button.pack()

        # Entry for removing flavors
        self.remove_flavor_entry = tk.Entry(root)
        self.remove_flavor_entry.pack()
        self.remove_flavor_entry.insert(0, "Введите сорт для удаления")

        # Button to remove flavor
        self.remove_flavor_button = tk.Button(root, text="Удалить сорт", command=self.remove_flavor)
        self.remove_flavor_button.pack()

        # Initial load of flavors
        self.refresh_flavors()

    def refresh_flavors(self):
        """Обновляет список доступных сортов мороженого."""
        self.flavor_listbox.delete(0, tk.END)  # Очистка списка
        for flavor in self.stand.get_flavors():
            self.flavor_listbox.insert(tk.END, flavor)  # Добавление сортов в список

    def add_flavor(self):
        """Добавляет новый сорт мороженого."""
        new_flavor = self.new_flavor_entry.get()
        if new_flavor and self.stand.add_flavor(new_flavor):
            messagebox.showinfo("Успех", f"Сорт '{new_flavor}' добавлен.")
            self.refresh_flavors()
        else:
            messagebox.showwarning("Ошибка", f"Сорт '{new_flavor}' уже существует.")

    def remove_flavor(self):
        """Удаляет сорт мороженого."""
        flavor_to_remove = self.remove_flavor_entry.get()
        if flavor_to_remove and self.stand.remove_flavor(flavor_to_remove):
            messagebox.showinfo("Успех", f"Сорт '{flavor_to_remove}' удален.")
            self.refresh_flavors()
        else:
            messagebox.showwarning("Ошибка", f"Сорт '{flavor_to_remove}' не найден.")

if __name__ == "__main__":
    root = tk.Tk()
    app = IceCreamApp(root)
    root.mainloop()
