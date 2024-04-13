#Напишите функцию на Python, которая принимает список чисел и возвращает новый список, содержащий только уникальные значения исходного списка.
def get_unique_list(input_list):
    return list(set(input_list))

print(get_unique_list([1, 2, 3, 3, 3, 3, 4, 5]))