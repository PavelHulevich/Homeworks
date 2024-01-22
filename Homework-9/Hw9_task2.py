"""Задание 2:
Напишите функцию sort_by_length(lst: list) -> list, которая принимает в качестве аргумента
список строк lst и возвращает новый список, отсортированный по длине строк в
возрастающем порядке не меняя исходный список. В функции нельзя использовать циклы.
Например, sort_by_length(["apple", "banana", "cherry", "date"]) должна вернуть ["date", "apple",
"banana", "cherry"]."""
from random import choice
from time import sleep


def sort_by_length(lst: list) -> list:
    list_out = lst.copy()
    list_out.sort(key=len)
    return list_out


def is_validate_data(list_in: list) -> bool:
    # Проверка валидности исходных данных. На выходе False - если ошибка входных данных.
    if not isinstance(list_in, list):
        print('Ошибка. На входе не список')
        return False
    for string in list_in:
        if not isinstance(string, str):
            print('Ошибка. В списке не строки')
            return False
    return True  # No errors


def sort_by_length_entry(list_in: list) -> None:
    print('\nВведен список строк: ', list_in)
    if is_validate_data(list_in):
        print('Результат сортировки:', sort_by_length(list_in))
    else:
        print('Неверные входные данные')


TEST_LIST = [['ccccc', 'bbbb', 'aaa', 'aa'], ['aaaaa', 'aaaa', 'aa', 'aaaa'],
             ['исходный', 'список', 'не', 'меняя'], ["apple", "banana", "cherry", "date"], 'a', 25, {22, 34}]
while True:
    sort_by_length_entry(choice(TEST_LIST))
    sleep(2)
