"""
Задание 6:
Напишите программу, которая читает pickle-файл, содержащий матрицу (список списков
чисел) и выводит на экран ее определитель. Если матрица не квадратная, то программа
должна вывести сообщение об ошибке.
"""
from random import randint
import os
import pickle
from time import sleep


def calculating_matrix_determinant(pickle_name: str) -> int:
    # Чтение pickle-файла с двумерным списком и вычисление определителя матрицы.
    with open(pickle_name, 'rb') as infile:
        matrix = pickle.load(infile)
    print('Из файла прочитана матрица: \n', matrix[0], '\n', matrix[1])
    determinant = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    return determinant


def writing_pickle(matrix_out: list) -> str:
    # Запись матрицы в pickle-файл и выдача на выход имени файла.
    if os.path.isfile('matrix.pickle'):
        os.remove('matrix.pickle')
    # Сериализация и запись словарей в файл.
    with open('matrix.pickle', 'wb') as outfile:
        pickle.dump(matrix_out, outfile)
    return 'matrix.pickle'


def validate_enter_data(list_1: list, list_2: list) -> bool:
    if not isinstance(list_1, list) or not isinstance(list_2, list):
        print('Ошибка. На входе не список')
        return False
    if len(list_1) != 2 or len(list_2) != 2:
        print('Ошибка. Матрица не квадратная')
        return False
    for index_1 in list_1:
        for index_2 in list_2:
            if not isinstance(index_2, int) or not isinstance(index_1, int):
                print('Ошибка. В списке не целые числа')
                return False
    return True


def calculating_matrix_determinant_enter(list_1: list, list_2: list) -> int:
    validate_result = validate_enter_data(list_1, list_2)
    if validate_result:
        matrix = [list_1, list_2]
        pickle_name = writing_pickle(matrix)  # Сериализация матрицы в pickle-файл.
        determ = calculating_matrix_determinant(pickle_name)
        print('Определитель матрицы равен:', determ, '\n')
        return determ
    else:
        print(f'Введены списки:   {list_1},   и:   {list_2}')
        print('Введены неверные данные\n')


TEST_LIST_OF_LISTS = [[1, 2], [-2, 3], [4, -5], [4, 7], [-8, 9], [10, -11], [11, 12], [-12, 13],
                      [1, 'a'], [2, 3], ['say', 5], 25, {8, 9}, 'day', [11, 12],
                      [12, 13, 5], [10, 11, 8], [11, 12, 7], [12, 13], [8, -9], [-10, 11], [-11, 12]]
# Тестовые прогоны.
if calculating_matrix_determinant_enter([11, -3], [-15, -2]) != -67:
    print('Ошибка в работе логики программы')
    exit()
while True:
    list_index_1 = randint(0, len(TEST_LIST_OF_LISTS)) - 1
    list_index_2 = randint(0, len(TEST_LIST_OF_LISTS)) - 1
    calculating_matrix_determinant_enter(TEST_LIST_OF_LISTS[list_index_1], TEST_LIST_OF_LISTS[list_index_2])
    sleep(3)