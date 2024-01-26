"""Задание 8*:
Напишите функцию для вычисления суммы чисел списка с поддержкой вложенных списков с
помощью рекурсии. Программа должна выбрасывать исключение в случае, если в списке
будет встречаться не числа."""
from typing import List, Any
from time import sleep
import sys


def calc_sum_list(list_in: List[int]) -> int:
    # Вычисление суммы всех элементов списка, включая элементы всех вложенных списков (рекурсия).
    if isinstance(list_in[0], list):
        list_in[0] = calc_sum_list(list_in[0])
    if len(list_in) < 2:
        return list_in[0]
    else:
        try:
            return list_in[0] + calc_sum_list(list_in[1:])
        except TypeError:
            print(f'СРАБОТАЛО ИСКЛЮЧЕНИЕ: {sys.exc_info()[0]}  В списке содержится не число')
            return 0


def is_validate_data(list_in: Any) -> bool:
    # Проверка валидности исходных данных. На выходе False - если ошибка входных данных.
    if not isinstance(list_in, list):
        print('Ошибка. На входе не список')
        return False
    for index in list_in:
        if isinstance(index, list):
            if not is_validate_data(index):
                print('Вложенный список содержит недопустимые данные')
                return False
            else:
                continue
        # if not isinstance(index, int):
        #     print('В списке содержится не целое число')
        #     return False
    return True


def calc_sum_list_entry(list_in: Any) -> None:
    print(f'\nВведены денные: {list_in}')
    if is_validate_data(list_in):
        result = calc_sum_list(list_in)
        print(f'Сумма всех значений в списке и всех вложенных списках: {result}')
    else:
        print('Неверные входные данные')


TEST_LIST = [[2, 2, 2, [3, 5, 6, [3, 5]], [3, 5]], [3, 5, 6, [3, 5]], [3, 5, 6, ], 25, [[[3, 4], [3, 4]], [1, 2]],
             'say', {2, 3}, 122, False, [[3, 5], [3, 5]], [[3, 'a'], [3, 5]], [[3, 5], ['day', 5]]]
for index in TEST_LIST:
    calc_sum_list_entry(index)
    sleep(1)
