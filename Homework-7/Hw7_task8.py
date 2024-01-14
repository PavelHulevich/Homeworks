"""
Задание 8:
Напишите программу, которая принимает на вход два словаря и объединяет их в один
словарь, в котором ключи и значения из первого словаря перезаписываются ключами и
значениями из второго словаря, если они совпадают. Программа должна выводить на экран
полученный словарь. Пример ввода и вывода:
Введите первый словарь: {'a': 1, 'b': 2, 'c': 3}
Введите второй словарь: {'b': 4, 'd': 5}
Объединенный словарь: {'a': 1, 'b': 4, 'c': 3, 'd': 5}
"""
from random import randint
from time import sleep


def merging_dictionaries(dict_1, dict_2):
    for i in dict_2.keys():
        dict_1[i] = dict_2[i]
    return dict_1


def validate_enter_data(dict_1, dict_2):
    if not isinstance(dict_1, dict) or not isinstance(dict_2, dict):
        print('Ошибка. На входе не словарь')
        return False
    return True


def merging_dictionaries_enter(dict_1, dict_2):
    validate_result = validate_enter_data(dict_1, dict_2)
    print(f'Введены словари:   {dict_1},   и:   {dict_2}')
    if validate_result:
        dict_result = merging_dictionaries(dict_1, dict_2)
        print(f'Словарь после объединения: {dict_result}\n')
    else:
        print('Введены неверные данные\n')


test_list_of_dict = [{'a': 1, 'b': 2, 'c': 3}, {'a': 25, 'd': 5, 'e': 37}, {'a': 31, 'b': 85, 'c': 46},
                     {'a': 31, 'b': 85, 'c': 46}, {'b': 4, 'd': 5}, [1, 5, 7], 'say', 25]
while True:
    dict_index_1 = randint(0, len(test_list_of_dict))-1
    dict_index_2 = randint(0, len(test_list_of_dict))-1
    merging_dictionaries_enter(test_list_of_dict[dict_index_1], test_list_of_dict[dict_index_2])
    sleep(3)
