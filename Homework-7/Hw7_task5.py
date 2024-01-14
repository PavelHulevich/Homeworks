"""
Задание 5:
Напишите программу, которая принимает на вход кортеж чисел и выводит на экран индекс и
значение максимального числа в кортеже. Программа должна использовать цикл for и
переменные для хранения индекса и значения максимального числа. Программа не должна
использовать встроенную функцию max для поиска максимального числа в кортеже.
"""
from time import sleep


def find_max_item_index(tuple_in):
    max_item_index = 0
    for index in range(len(tuple_in)):
        if tuple_in[index] > tuple_in[max_item_index]:
            max_item_index = index
    return max_item_index


def validate_enter_data(tuple_in):
    if not isinstance(tuple_in, tuple):
        print('Ошибка. На входе не кортеж')
        return False
    for i in tuple_in:
        if not isinstance(i, (int, float)):
            print('Ошибка. В кортеже находится не число')
            return False
    return True


def find_max_item_entrance(tuple_in):
    validate_result = validate_enter_data(tuple_in)
    if validate_result:
        max_item_index = find_max_item_index(tuple_in)  #
        print(f'Для кортежа чисел: {tuple_in}', end='')
        print(f' Индекс максимального числа: {max_item_index},'
              f'  Значение максимального числа:  {tuple_in[max_item_index]} \n')
    else:
        print(f'Ошибка, в кортеже: {tuple_in} Входные данные не верны\n')


test_lists = [(77, 25, 66, 123), (3, 67, 34, 78), 45,
              (64, 29, 'say', 345), (67, 35, 11, 112), (42, 96, 47, 134), (345, 653), (93, 475, 322)]
for index in test_lists:
    find_max_item_entrance(index)
    sleep(3)
