"""
Задание 4:
Напишите программу, которая принимает на вход многомерный список, состоящий из
списков чисел, и выводит на экран список, который состоит из максимальных элементов
каждого вложенного списка.
Пример: если на вход подан список [[1, 2, 3], [4, 5, 6], [7, 8, 9]], то на выходе должен быть
список [3, 6, 9].
"""


def find_max_items(two_dim_list):
    max_items_list = []
    for i in two_dim_list:
        max_items_list.append(max(i))
    return max_items_list


def checking_input_data(two_dim_list):
    if not isinstance(two_dim_list, list):
        print('На входе не список')
        return False
    for i in two_dim_list:
        if not isinstance(i, list):
            print("Список первого уровня содержит не список")
            return False
        for j in i:
            if not isinstance(j, (int, float)):
                print('В элементах списка содержится не число')
                return False
    return True


def find_max_items_entrance(two_dim_list):
    # Проверяем валидность входных данных. Если данные не соответствуют - на выходе False
    # Иначе - На выходе список с максимальными значениями из всех списков второго уровня.
    check_result = checking_input_data(two_dim_list)
    if check_result:
        return find_max_items(two_dim_list)
    else:
        return check_result


tests_two_dim_list = ([[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3, 56], [4, 95, 6], [7, 8, 9]],
                [[1, 'j', 3], [4, 5, 6], [7, 8, 9], [1, 2, 3, 56], [4, 95, 6], [7, 8, 9]],
                [[1, 2, 3], 25, [7, 8, 9], [1, 2, 3, 56], [4, 95, 6], [7, 8, 9]],
                45)
for i in tests_two_dim_list:
    print(i, '  ====>   ', find_max_items_entrance(i))
