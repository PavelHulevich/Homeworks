"""
Задание 6:
Напишите программу, которая вводит по строкам с клавиатуры двумерный массив и
вычисляет сумму его элементов по столбцам.
"""


def input_2dim_array():
    # Ввод с клавиатуры двумерного массива. С проверкой. На выходе двумерный массив
    while True:
        try:
            rows = int(input('Введите количество строк двумерного массива: '))
            cols = int(input('Введите количество столбцов двумерного массива: '))
            two_dim_array = [[0] * cols for _ in range(rows)]
            for row in range(rows):
                row_current = input(f'Введите {cols} целых числа строки № {row + 1} , разделяя числа пробелом: ')
                row_current_list = row_current.split(' ')
                for j in range(cols):
                    two_dim_array[row][j] = int(row_current_list[j])
        except ValueError:
            print('Введены недопустимые данные. Повторите ввод')
        else:
            return two_dim_array


def counting_sum_of_columns(two_dim_array):
    # Суммирование значений столбцов двумерного массива. На выходе - список со значениями сумм каждого столбца.
    sum_cols = [0 for _ in range(len(two_dim_array[0]))]
    for row in two_dim_array:
        for index_col in range(len(row)):
            sum_cols[index_col] += row[index_col]
    return sum_cols


def counting_sum_of_columns_entrance():
    # Вызывает ввод с клавиатуры двумерного массива. Считает сумму элементов каждого столбца отдельно
    # На выходе - список со значениями сумм каждого столбца.
    two_dim_array = input_2dim_array()
    sum_cols = counting_sum_of_columns(two_dim_array)
    print('Input array: ')
    for i in two_dim_array:
        print(i)
    print(f'Result: \n{sum_cols}')
    return sum_cols


# Тестовые прогоны
while True:
    counting_sum_of_columns_entrance()
    print('')
