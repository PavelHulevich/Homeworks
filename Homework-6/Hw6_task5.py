"""
Задание 5:
Напишите программу, которая принимает на вход многомерный список, состоящий из
списков чисел, и выводит на экран транспонированный список. То есть список, в котором
строки и столбцы поменяны местами.
Пример: если на вход подан список [[1, 2, 3], [4, 5, 6], [7, 8, 9]], то на выходе должен быть
список [[1, 4, 7], [2, 5, 8], [3, 6, 9]].
"""


def transpose_2dim_list(list_in):
    # Транспонирование списка
    size = len(list_in)
    b = [[0] * size for _ in range(size)]
    for i in range(3):
        for j in range(3):
            b[i][j] = list_in[j][i]
    return b


def checking_input_data(two_dim_list):
    # Проверяет аргумент, на соответствие требованиям. 0 - если нет ошибки, иначе - код ошибки
    if not isinstance(two_dim_list, list):
        print("На входе не список")
        return False
    for i in two_dim_list:
        if not isinstance(i, list):
            print("Список первого уровня содержит не список")
            return False
        if len(i) != len(two_dim_list):
            print('Количество строк не совпадает с количеством столбцов')
            return False
        for j in i:
            if not isinstance(j, (int, float)):
                print('В элементах списка содержится не число')
                return False
    return True


def transpose_2dim_list_entrance(two_dim_list):
    # Проверяем валидность входных данных. Если данные не соответствуют - False
    # Иначе - выполняем транспонирование и передаем на выход результирующей список.
    check_result = checking_input_data(two_dim_list)
    if check_result:
        return transpose_2dim_list(two_dim_list)
    else:
        return 'Ошибка входных данных'


# Тестовые прогоны
test_lists_in = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                 [[1, 2, 'a'], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5], [7, 8, 9]],
                 [[1, 2, 3], 8, [7, 8, 9]], 25]
for x in test_lists_in:
    print(x, '  ====>  ', transpose_2dim_list_entrance(x))
