"""
Задание 5:
Напишите программу, которая сравнивает два json-файла, содержащих словари, и выводит на
экран различия между ними. Например, если файлы содержат словари {"a": 1, "b": 2, "c": 3} и
{"a": 1, "b": 4, "d": 5}, то программа должна вывести "Ключи b и c разные, ключ d отсутствует
в первом файле"
"""
from random import randint
import os
import json
from time import sleep
"""
После запуска происходит бесконечный цикл с задержкой в 3 секунды с произвольной выборкой двух словарей
 из списка валидных и невалидных вариантов 
"""


def writing_2json(dict_1_out: dict, dict_2_out: dict) -> list:
    # Сериализация двух словарей в json-файлы: 'dict_1.json' и 'dict_1.json'
    # Удаление старых файлов, если они были в папке.
    if os.path.isfile('dict_1.json'):
        os.remove('dict_2.json')
    if os.path.isfile('dict_2.json'):
        os.remove('dict_2.json')

    # Сериализация и запись словарей в файл.
    with open('dict_1.json', 'w') as outfile:
        json.dump(dict_1_out, outfile)
    with open('dict_2.json', 'w') as outfile:
        json.dump(dict_2_out, outfile)
    return ['dict_1.json', 'dict_2.json']


def matching_json_files(json_names: list) -> None:
    # Десериализация двух файлов, имена которых предаются в списке и сравнение полученных словарей.
    # Десериализация двух файлов в словари.
    with open(json_names[0]) as infile:
        dict_1 = json.load(infile)
    with open(json_names[1]) as infile:
        dict_2 = json.load(infile)
    # Сравнение двух полученных словарей.
    print(f'Первый файл: {dict_1}')
    print(f'Второй файл: {dict_2}')
    if dict_2 != dict_1:
        if dict_2.keys() - dict_1.keys():
            print(f'Ключи {dict_2.keys() - dict_1.keys()} из второго файла отсутствуют в первом файле' )
        if dict_1.keys() - dict_2.keys():
            print(f'Ключи {dict_1.keys() - dict_2.keys()} из первого файла отсутствуют во втором файле')
        print('Ключи, значение которых отличаются в двух словарях: ', end=' ')
        for k1, v1 in dict_1.items():
            for k2, v2 in dict_2.items():
                if k1 == k2 and v1 != v2:
                    print(f'"{k1}"', end=' ')
        print('\n')
    else:
        print('Словари идентичны')


def validate_enter_data(dict_1: dict, dict_2: dict) -> bool:
    if not isinstance(dict_1, dict) or not isinstance(dict_2, dict):
        print('Ошибка. На входе не словарь')
        return False
    return True


def matching_json_files_enter(dict_1: dict, dict_2: dict) -> None:
    validate_result = validate_enter_data(dict_1, dict_2)
    if validate_result:
        json_names = writing_2json(dict_1, dict_2)  # Сериализация двух словарей в json-файлы. Получаем список с именами
        matching_json_files(json_names)                 # двух файлов
    else:
        print(f'Введены словари:   {dict_1},   и:   {dict_2}')
        print('Введены неверные данные\n')


TEST_LIST_OF_DICT = [{'a': 1, 'b': 2, 'c': 3}, {'a': 25, 'd': 5, 'e': 37}, {'a': 31, 'b': 85, 'c': 46},
                     {'a': 31, 'b': 85, 'c': 46}, {'b': 4, 'd': 5}, [1, 5, 7], 'say', 25,
                     {"a": 1, "b": 2, "c": 3, "f": 9}, {"a": 1, "b": 4, "d": 5, "f": 10},
                     {'a': 1, 'b': 2, 'c': 5}, {'a': 1, 'b': 77, 'c': 3}, {'a': 35, 'b': 2, 'c': 3},
                     {'a': 1, 'b': 2, 'c': 5, 'j': 9}, {'a': 1, 'b': 77, 'c': 3, 'r': 8},
                     {'a': 35, 'b': 2, 'c': 3, 'e': 4}, {'a': 35, 'b': 2, 'c': 3, 'w': 6 }]
# Тестовые прогоны.
while True:
    dict_index_1 = randint(0, len(TEST_LIST_OF_DICT)) - 1
    dict_index_2 = randint(0, len(TEST_LIST_OF_DICT)) - 1
    matching_json_files_enter(TEST_LIST_OF_DICT[dict_index_1], TEST_LIST_OF_DICT[dict_index_2])
    sleep(3)
