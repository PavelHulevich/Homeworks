"""
Задание 2:
Напишите программу, которая принимает на вход два кортежа одинаковой длины и выводит
на экран кортеж, который состоит из произведения соответствующих элементов этих
кортежей. Пример: если на вход поданы кортежи (1, 2, 3) и (4, 5, 6), то на выходе должен быть
кортеж (4, 10, 18). Программа должна использовать цикл for и оператор * для умножения
элементов кортежей.
"""
from random import randint
from time import sleep


def multiplying_tuples(tuple_1, tuple_2):
    list_1 = list(tuple_1)
    list_2 = list(tuple_2)
    list_3 = [0 for _ in range(len(tuple_1))]
    for index in range(len(tuple_1)):
        list_3[index] = list_1[index] * list_2[index]
    return tuple(list_3)


def validate_enter_data(tuple_1, tuple_2):
    # Проверка валидности исходных данных. На выходе False - если ошибка входных данных.
    if not isinstance(tuple_1, tuple) or not isinstance(tuple_2, tuple):
        print('Ошибка. На входе не кортеж')
        return False
    if len(tuple_1) != len(tuple_2):
        print('Ошибка. На входе кортежи разной длины')
        return False
    for i in range(len(tuple_1)):
        if not isinstance(tuple_1[i], (int, float)) or not isinstance(tuple_2[i], (int, float)):
            print("Ошибка. Кортеж содержит не число")
            return False
    return True  # No errors


def multiplying_tuples_entrance(tuple1, tuple_2):
    validate_result = validate_enter_data(tuple1, tuple_2)
    if validate_result:
        print(f'Для кортежей чисел: \n{tuple1}\n{tuple_2}\nПроизведение равно:')
        print(multiplying_tuples(tuple1, tuple_2), '\n')

    else:
        print(f'Ошибка, в кортежах:  \n{tuple1}\n{tuple_2}\nВходные данные не верны\n')


test_list = [25, 'say', (1, 'day', 3), (4, 5, 6, 7), (1, 2, 3, 8), (4, 5, 6, 2), (1, 2, 3, 8), (4, 5, 6, 7),
             (5, 6, 7), (2, 3, 8), (5, 6, 2), (2, 3, 8), (5, 6, 7)]
test_list_len = len(test_list)
while True:
    test_tuple_1 = test_list[randint(0, test_list_len - 1)]
    test_tuple_2 = test_list[randint(0, test_list_len - 1)]
    multiplying_tuples_entrance(test_tuple_1, test_tuple_2)
    sleep(3)
