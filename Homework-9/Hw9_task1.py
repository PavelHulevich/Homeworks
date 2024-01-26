"""
Задание 1:
Напишите рекурсивную функцию power(x, y) возвращающего результат возведения числа x в
степень y
"""
from typing import Any
from random import choice
from time import sleep


def power(x: (int, float), y: (int, float)) -> (int, float):
    if y <= 1:
        return x
    else:
        return x * power(x, y-1)


def is_validate_data(number_1: Any, number_2: Any) -> bool:
    # Проверка валидности исходных данных. На выходе False - если ошибка входных данных.
    if not isinstance(number_1,  (int, float)) or not isinstance(number_2,  (int, float)):
        print('Ошибка. На входе не число')
        return False
    return True  # No errors


def calculating_degree_number(number_1: Any, number_2: Any) -> None:
    print(f'\n Введены значения: "{number_1}"   и  "{number_2}"  ')
    validation_result = is_validate_data(number_1, number_2)
    if validation_result:
        result = power(number_1, number_2)
        print(f'Число {number_1} в степени числа {number_2} равно {result} ')
    else:
        print('Введены неверные значения')


# Тестовые прогоны
TEST_LIST = [2, 3, 4, 5, 6, 7, 8, 9, 'a', 'say', [1, 2, 3], 5.2, 1.3, 4.2, {2, 1}, False]
while True:
    calculating_degree_number(choice(TEST_LIST), choice(TEST_LIST))
    sleep(2)
