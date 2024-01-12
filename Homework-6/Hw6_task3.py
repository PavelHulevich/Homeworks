"""
Задание 3:
Напишите программу, которая принимает на вход список чисел и выводит на экран
максимальное и минимальное число в списке. Программа не должна использовать
встроенные функции max и min для поиска максимума и минимума.
"""

def checking_input_data(number_list):
    if not isinstance(number_list, list):
            print('На входе не список')
            return 100
    for i in number_list:
        if not isinstance(i, (int, float)):
            print('В списке находится не число')
            return 101
    return 0

def find_max_min(number_list):
    # Method 1. Simplest
    number_list.sort()
    print(number_list[0], number_list[-1])

    # Method 2. For-Cycle
    max_num = number_list[0]
    min_num = number_list[0]
    for i in number_list:
        if i < min_num:
            min_num = i
        if i > max_num:
            max_num = i
    print(min_num, max_num)

    # Method 3. While-Cycle
    max_num = number_list[0]
    min_num = number_list[0]
    i = 0
    while i < len(number_list):
        if number_list[i] < min_num:
            min_num = number_list[1]
        if number_list[i] > max_num:
            max_num = number_list[i]
        i += 1
    print(min_num, max_num)


def find_max_min_entrance(list):
    # Проверяем валидность входных данных. Если данные не соответствуют - передаем на выход код ошибки
    # Иначе - выполняем печать крайних значений. На выходе - 0.
    check_result = checking_input_data(list)
    if check_result != 0:
        return check_result
    else:
        find_max_min(list)
        return 0


number_list = [34, 87, 5.3, 475, 56, 765, 321]
find_max_min_entrance(number_list)