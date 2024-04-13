#Класс для управления запасами продуктов
#Цель: Напишите класс Inventory, который позволит добавлять продукты (с именем и количеством)
# в инвентарь и удалять их оттуда по имени.
#Основные требования:
#Метод add_product(name, quantity) для добавления продуктов.
#Метод remove_product(name) для удаления продукта по имени.
#Метод get_inventory() для получения словаря с текущим состоянием инвентаря.

class Inventory:
    def __init__(self):
        # Инициализация пустого инвентаря
        self.products = {}

    def add_product(self, name, quantity):
        """Добавляет продукт с указанным количеством в инвентарь. Если продукт уже существует, его количество увеличивается."""
        if name in self.products:
            self.products[name] += quantity
        else:
            self.products[name] = quantity

    def remove_product(self, name):
        """Удаляет продукт из инвентаря по имени."""
        if name in self.products:
            del self.products[name]
        else:
            print(f"Продукт '{name}' не найден в инвентаре.")

    def get_inventory(self):
        """Возвращает текущее состояние инвентаря."""
        return self.products


# Пример использования класса Inventory
inventory = Inventory()
inventory.add_product("Яблоки", 10)
inventory.add_product("Бананы", 5)
inventory.add_product("Яблоки", 5)  # Добавит 5 еще, в результате станет 15 яблок

print(inventory.get_inventory())  # Выведет {'Яблоки': 15, 'Бананы': 5}

inventory.remove_product("Бананы")
print(inventory.get_inventory())  # Выведет {'Яблоки': 15}, так как бананы были удалены

inventory.remove_product("Апельсины")  # Продукт 'Апельсины' не найден в инвентаре.