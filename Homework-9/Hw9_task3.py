"""Задание 3:
Напишите функцию map_square(lst: list) -> list, которая принимает в качестве аргумента
список чисел lst и возвращает новый список, содержащий квадраты чисел из lst. В функции
нельзя использовать циклы. Например, map_square([1, 2, 3, 4, 5]) должна вернуть [1, 4, 9, 16,
25].
"""
from random import choice
from time import sleep


def map_square(list_in: list[int]) -> list[int]:
    list_out = [i * i for i in list_in]
    return list_out


def is_validate_data(list_in: list) -> bool:
    # Проверка валидности исходных данных. На выходе False - если ошибка входных данных.
    if not isinstance(list_in, list):
        print('Ошибка. На входе не список')
        return False
    for number in list_in:
        if not isinstance(number, int):
            print('Ошибка. В списке не целые числа')
            return False
    return True  # No errors


def map_square_entry(list_in: list) -> None:
    print('\nВведен список: ', list_in)
    if is_validate_data(list_in):
        print('Квадраты содержимого списка равны списку: ', map_square(list_in))
    else:
        print('Не верные входные данные')


TEST_LIST = [[1, 2, 3, 4, 5], [5, 3, 4, 7, 9], [12, 10, 11], 'A', 'day', 25, {23, 5}]
while True:
    map_square_entry(choice(TEST_LIST))
    sleep(2)
