"""
Задание 8:
Написать программу, которая объединяет два упорядоченных по возрастанию массива чисел
в один, который также должен быть упорядочен по возрастанию.
"""
# # # Method 1. Simplest for Python
# a.extend(b)
# a.sort()
# print(a)

# Method 2.
def sorting_list(list):
    while True:         # Implementing cycle do-while.
        flag = True
        for i in range(len(list) - 2):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                flag = False
        if flag: break  # Perform a bubble sort on the list. Until an idle pass occurs (stay True).
    return list


def checking_input_data(list_1, list_2):
    if not isinstance(list_1, list) or not isinstance(list_2, list):
            print('На входе не список')
            return 100
    for i in list_1:
        if not isinstance(i, (int, float)):
            print('В списке 1 находится не число')
            return 101
    for i in list_2:
        if not isinstance(i, (int, float)):
            print('В списке 2 находится не число')
            return 101
    return 0


def sorting_lists_entrance(list_1, list_2):
    # Проверяем валидность входных данных. Если данные не соответствуют - передаем на выход код ошибки
    # Иначе - на выходе общий отсортированный список.
    check_result = checking_input_data(list_1, list_2)
    if check_result != 0:
        return check_result
    else:
        list1_sort = sorting_list(list_1)
        list2_sort = sorting_list(list_2)
        common_list = list1_sort + list2_sort
        common_list_sort = sorting_list(common_list)
        return common_list_sort

list_1 = [125, 135, 127, 145, 150, 130, 140, 132]
list_2 = [77, 25, 66, '88', 56, 2, 500]
common_list_sort = sorting_lists_entrance(list_1, list_2)
print(f'List 1: {list_1}\n')
print(f'List 2: {list_2}\n')
print(f'Common sorted list: {common_list_sort}')



