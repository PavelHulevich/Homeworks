"""Задание 4:
Напишите функцию count_vowels(s: str, case_sensitive: bool = False) -> int, которая возвращает
количество уникальных гласных букв в строке s. Гласными буквами считаются 'a', 'e', 'i', 'o',
'u'. Аргумент case_sensitive определяет, учитывать ли регистр букв при подсчете. Если
case_sensitive равен False, то функция должна игнорировать регистр букв и считать 'A' и 'a'
одинаковыми. Если case_sensitive равен True, то функция должна различать регистр букв и
считать 'A' и 'a' разными. Например, count_vowels("Hello, world!", case_sensitive=True) должна
вернуть 2, так как в строке есть только две гласные буквы 'e' и 'o'.
"""
from typing import Any
from random import choice
from time import sleep


def count_vowels(string_in: str, case_sensitive: bool = False) -> int:
    vowels_low = ['a', 'e', 'i', 'o', 'u']
    vowels_caps = ['A', 'E', 'I', 'O', 'U']
    if case_sensitive:
        vowels_set = {i for i in string_in if i in vowels_low or i in vowels_caps}
    else:
        vowels_set = {i.lower() for i in string_in if i in vowels_low or i in vowels_caps}
    return len(vowels_set)


def is_validate_data(string_in: Any, flag: Any) -> bool:
    # Проверка валидности исходных данных. На выходе False - если ошибка входных данных.
    if not isinstance(string_in, str):
        print('Ошибка. На входе не строка')
        return False
    if not isinstance(flag, bool):
        print('Ошибка. Второй аргумент не логический')
        return False
    return True  # No errors


def count_vowels_entry(string_in: Any, case_sensitive: Any = False) -> None:
    print(f'\nВведены данные : "{string_in}", {case_sensitive}. Регистр букв ', end='')
    if case_sensitive:
        print('РАЗЛИЧАЕТСЯ')
    else:
        print('НЕ РАЗЛИЧАЕТСЯ')
    if is_validate_data(string_in, case_sensitive):
        print('Количество гласных букв во введенной строке: ', count_vowels(string_in, case_sensitive))
    else:
        print('Неверные входные данные')


TEST_LIST = ["Hello, world!", "Hello, WORLD!", 'map_square', 'from time import sleep', 'from time IMPORT SLEEP',
             'case_sensitive', 'case_SENSITIVE', 23, [15, 25], ['say', 45], {4, 5}]
while True:
    count_vowels_entry(choice(TEST_LIST), choice([True, False, 'case_SENSITIVE', 23, [15, 25], ['say', 45],
                                                  True, False, True, False, {4, 5}]))
    sleep(3)
