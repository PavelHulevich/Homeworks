"""Задание 6:
Напишите функцию для разворота числа (представления числа в обратном порядке) с
помощью рекурсии. В решении можно пользоваться только типом int и никакими другими
типами данных."""
from typing import Any
from random import randint


def reverse_number(integer_in: int, integer_out: int = 0) -> int:
    if not integer_in:
        return integer_out
    integer_out = integer_out*10 + integer_in % 10
    return reverse_number(integer_in // 10, integer_out)


def is_validate_data(number: Any) -> bool:
    # Проверка валидности исходных данных. На выходе False - если ошибка входных данных.
    if not isinstance(number, int):
        print('Ошибка. На входе не целое число')
        return False
    return True  # No errors


def reverse_number_entry(number: Any) -> None:
    print(f'\nВведены данные: {number}.  ', end='')
    if is_validate_data(number):
        print('Обратное число: ', reverse_number(number))
    else:
        print('Введены неверные данные')


TEST_LIST = [123, 'A', 'say', {1, 2, 4}, 15.24, 456789, 8, [123, 56], 123456, 789]
for i in range(0, len(TEST_LIST)):
    reverse_number_entry(randint(11, 9999999))
    reverse_number_entry(TEST_LIST[i])
