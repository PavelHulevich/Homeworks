"""
Задание 5:
Напишите программу, которая принимает на вход многомерный список, состоящий из
списков чисел, и выводит на экран транспонированный список, то есть список, в котором
строки и столбцы поменяны местами.
Пример: если на вход подан список [[1, 2, 3], [4, 5, 6], [7, 8, 9]], то на выходе должен быть
список [[1, 4, 7], [2, 5, 8], [3, 6, 9]].
"""


def swap(list):
    size = len(list)
    b = [[0] * size for _ in range(size)]
    for i in range(3):
        for j in range(3):
            b[i][j] = list[j][i]
    return b


def checking_input_data(two_dim_list):
    if not isinstance(two_dim_list, list):
        print("На входе не список")
        return 0b0001
    for i in two_dim_list:
        if not isinstance(i, list):
            print("Список первого уровня содержит не список")
            return 0b0010
        if len(i) != len(two_dim_list):
            print('Количество строк не совпадает с количеством столбцов')
            return 0b0100
        for j in i:
            if not isinstance(j, (int, float)):
                print('Элементы списка не являются числом')
                return 0b1000
    return 0


def swap_rows_and_columns(two_dim_list):
    check_result = checking_input_data(two_dim_list)
    if check_result != 0:
        return check_result
    else:
        return swap(two_dim_list)




