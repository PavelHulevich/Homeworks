"""
Задание 8:
Написать программу, которая объединяет два упорядоченных по возрастанию массива чисел
в один, который также должен быть упорядочен по возрастанию.
"""


# Способ 1. Простейший для Пайтона
# a.extend(b)
# a.sort()
# print(a)


# Спобос 2.
def sorting_list(list_in):
    while True:
        is_all_sorted = True    # Флаг полной сортировки. Начально True, иначе цикл проверок не закончится.
        for i in range(len(list_in) - 2):
            if list_in[i] > list_in[i + 1]:
                list_in[i], list_in[i + 1] = list_in[i + 1], list_in[i]
                is_all_sorted = False  # Если была сортировка хотя бы в одном месте. То требуется повторный прогон.
        if is_all_sorted:   # Если в ходе прохода списка сортировок не произошло. Выход из цикла.
            break
    return list_in


def checking_input_data(list_1, list_2):
    if not isinstance(list_1, list) or not isinstance(list_2, list):
        print('Ошибка. На входе не список')
        return False
    for i in list_1:
        if not isinstance(i, (int, float)):
            print('Ошибка. В списке 1 находится не число')
            return False
    for i in list_2:
        if not isinstance(i, (int, float)):
            print('Ошибка. В списке 2 находится не число')
            return False
    return True


def sorting_lists_entrance(list_1, list_2):
    # Проверяем валидность входных данных. Если данные не соответствуют - передаем на выход код ошибки
    # Иначе - на выходе общий отсортированный список.
    check_result = checking_input_data(list_1, list_2)
    print(f'List 1: {list_1}')
    print(f'List 2: {list_2}\n')
    if not check_result:
        return check_result
    else:
        list1_sort = sorting_list(list_1)
        list2_sort = sorting_list(list_2)
        common_list = list1_sort + list2_sort
        common_list_sort = sorting_list(common_list)
        print(f'Отсортированный общий список: {common_list_sort}\n')
        return common_list_sort


# Тестовые прогоны
from random import randint
from time import sleep

test_lists = [[77, 25, 66, 123], [3, 67, 34, 78], 45,
              [64, 29, 'say', 345], [67, 35, 11, 112], [42, 96, 47, 134], [345, 653], [93, 475, 322]]
test_len = len(test_lists)-1
while True:
    common_list_sort_test = sorting_lists_entrance(test_lists[randint(0, test_len)], test_lists[randint(0, test_len)])
    sleep(3)
