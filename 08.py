#Простая система управления библиотекой
#Цель: Создайте класс Library, который будет управлять книгами в библиотеке с возможностью добавления и удаления книг.
#Основные требования:
#Метод add_book(title) для добавления новой книги по названию.
#Метод remove_book(title) для удаления книги по названию.
#Метод list_books() для вывода списка всех книг в библиотеке.

class Library:
    def __init__(self):
        # Инициализация пустого списка книг
        self.books = []

    def add_book(self, title):
        """Добавляет новую книгу в библиотеку по названию."""
        self.books.append(title)
        print(f"Книга '{title}' успешно добавлена.")

    def remove_book(self, title):
        """Удаляет книгу из библиотеки по названию."""
        if title in self.books:
            self.books.remove(title)
            print(f"Книга '{title}' успешно удалена.")
        else:
            print(f"Книга '{title}' не найдена в библиотеке.")

    def list_books(self):
        """Выводит список всех книг в библиотеке."""
        if self.books:
            print("Список книг в библиотеке:")
            for book in self.books:
                print(book)
        else:
            print("Библиотека пуста.")

# Пример использования
# Создание экземпляра класса Library
my_library = Library()

# Добавление книг
my_library.add_book("1984")
my_library.add_book("Война и мир")
my_library.add_book("Гордость и предубеждение")

# Вывод списка всех книг в библиотеке
my_library.list_books()

# Удаление книги
my_library.remove_book("1984")

# Вывод списка книг после удаления одной из них
my_library.list_books()
