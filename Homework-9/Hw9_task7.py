"""Задание 7:
Напишите функцию modify_list(lst: list, *funcs: callable) -> None, которая принимает в
качестве аргументов список lst и произвольное количество функций funcs, и модифицирует
список lst так, что каждый его элемент преобразуется с помощью всех функций из funcs по
порядку. Функции из funcs должны принимать один аргумент и возвращать одно значение.
Функция modify_list не должна возвращать ничего, а изменять список lst на месте. Например,
modify_list([1, 2, 3], lambda x: x + 1, lambda x: x * 2) должна изменить список [1, 2, 3] на [4, 6,
8], так как каждый элемент сначала увеличивается на 1, а потом умножается на 2. Функции
для модификации элеметов списка:
• Возведение в квадрат четных чисел
• Увеличение на 1 нечетных чисел
• Умножение на 3 простых чисел"""
from typing import Any

def is_validate_data(list_in: Any) -> bool:
    # Проверка валидности исходных данных. На выходе False - если ошибка входных данных.
    if not isinstance(list_in, list):
        print('Ошибка. На входе не список')
        return False
    for number in list_in:
        if not isinstance(number, int):
            print('Ошибка. В списке не целые числа')
            return False
    return True  # No errors


def modify_list(lst: Any, *funcs: callable) -> None:
    print('\nВведены данные: ', lst)
    if not is_validate_data(lst):
        print('На входе неверные значения')
        return
    a = map(funcs[0], lst)
    a = map(funcs[1], a)
    a = map(funcs[2], a)
    print('Результат выполнения трех последовательных функций: ', list(a))


def square_of_even(num: int) -> int:
    if num % 2:
        return num
    else:
        return num * num


def increment_of_odd(num: int) -> int:
    if not num % 2:
        return num
    else:
        return num + 1


def is_simple(num: int) -> bool:
    if num == 1:
        return False  # 1 - не простое число
    for i in range(2, num // 2 + 1):
        if not num % i:
            return False  # Не простое число
    return True


def multiplication_3_of_simple(num: int) -> int:
    if is_simple(num):
        return num * 3
    else:
        return num


# Тестовые прогоны.
TEST_LIST = [[2, 4, 7, 9, 1], [1, 2, 3, 4, 5], [5, 3, 4, 7, 9], [12, 10, 11], 'A', 'day', 25, {23, 5}, [12, 'say', 11]]
for lst_in in TEST_LIST:
    modify_list(lst_in, square_of_even, increment_of_odd, multiplication_3_of_simple)
