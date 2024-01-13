"""
Задание 3:
Напишите программу, которая принимает на вход список чисел и выводит на экран
максимальное и минимальное число в списке. Программа не должна использовать
встроенные функции max и min для поиска максимума и минимума.
"""


def checking_input_data(list_in):
    if not isinstance(list_in, list):
        print('На входе не список')
        return False
    for i in list_in:
        if not isinstance(i, (int, float)):
            print('В списке находится не число')
            return False
    return True


def find_max_min(list_in):
    # Method 1. Simplest
    list_in.sort()
    print(list_in[0], list_in[-1])

    # Method 2. For-Cycle
    max_num = list_in[0]
    min_num = list_in[0]
    for i in list_in:
        if i < min_num:
            min_num = i
        if i > max_num:
            max_num = i
    print(min_num, max_num)

    # Method 3. While-Cycle
    max_num = list_in[0]
    min_num = list_in[0]
    i = 0
    while i < len(list_in):
        if list_in[i] < min_num:
            min_num = list_in[i]
        if list_in[i] > max_num:
            max_num = list_in[i]
        i += 1
    print(min_num, max_num)


def find_max_min_entrance(list_in):
    # Проверяем валидность входных данных. Если данные не соответствуют - передаем на выход False
    # Иначе - выполняем печать крайних значений. На выходе - True
    check_result = checking_input_data(list_in)
    if check_result:
        find_max_min(list_in)
    return check_result


number_list = [[34, 5.3, 475, 56, 765], [34, 's', 475, 56, 765], 25, 'swd',
               [34, 5.3, 475, 56, 765], [888, 5.3, 475, 56, 765]]
for x in number_list:
    print(x, find_max_min_entrance(x))
