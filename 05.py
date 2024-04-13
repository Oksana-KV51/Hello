#Создайте программу, которая анализирует заданную строку и выводит количество
# встречающихся в ней цифр, букв и специальных символов в сумме без учета пробелов.

def analyze_string(input_string):
    letters = 0
    digits = 0
    special_chars = 0

    # Проходим по каждому символу в строке
    for char in input_string:
        if char.isalpha():  # Проверяем, является ли символ буквой
            letters += 1
        elif char.isdigit():  # Проверяем, является ли символ цифрой
            digits += 1
        elif char != " ":  # Если символ не пробел, считаем его специальным символом
            special_chars += 1

    # Выводим результаты
    print(f"Букв: {letters}, Цифр: {digits}, Специальных символов: {special_chars}")


# Запрос ввода от пользователя
input_string = input("Введите строку для анализа: ")
analyze_string(input_string)