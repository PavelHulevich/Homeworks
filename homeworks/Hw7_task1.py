"""
Задание 1:
Напишите программу, которая принимает на вход список чисел, и выводит на экран кортеж,
который состоит из минимального и максимального числа в списке. Программа должна
использовать цикл for и не использовать встроенные функции min и max для поиска
минимума и максимума.
"""
from time import sleep


def find_min_max_tuple(list_in):
    min_max_list = [list_in[0], list_in[0]]
    for index in list_in:
        if index < min_max_list[0]:
            min_max_list[0] = index
        if index > min_max_list[1]:
            min_max_list[1] = index
    return tuple(min_max_list)


def validate_enter_data(list_in):
    # Проверка валидности исходных данных. На выходе False - если ошибка входных данных.
    if not isinstance(list_in, list):
        print('Ошибка. На входе не список')
        return False
    for i in list_in:
        if not isinstance(i, (int, float)):
            print("Ошибка. Список содержит не число")
            return False
    return True  # No errors


def find_min_max_tuple_entrance(list_in):
    validate_result = validate_enter_data(list_in)
    if validate_result:
        print(f'Для списка чисел: {list_in} минимальное и максимальное значение равно: {find_min_max_tuple(list_in)}\n')
    else:
        print(f'Ошибка, в списке {list_in} входные данные не верны\n')


# Тестовые прогоны
test_lists = [25, 'say', [12, 36, 48, 65, 75], [86, 2, 47, 36,], [852, 67, 49], [23, 45, 69, 78],
              [1, 's', 3], [3, 36, 'day', 'night', 75], [75, 2, 34, 36,], [578, 128, 49], [75, 45, 65, 78]]
for index in test_lists:
    find_min_max_tuple_entrance(index)
    sleep(3)
