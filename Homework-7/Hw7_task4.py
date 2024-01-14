"""
Задание 4:
Напишите программу, которая принимает на вход кортеж чисел и выводит на экран сумму
всех четных чисел в кортеже. Если в кортеже нет четных чисел, то программа выводит на
экран 0. Программа должна использовать цикл for и условный оператор if для проверки
четности числа. Программа должна использовать переменную для подсчета суммы четных
чисел.
"""
from time import sleep


def summing_even(tuple_in):
    summ_even = 0
    for index in tuple_in:
        if not index % 2:
            summ_even += index
    return summ_even


def validate_enter_data(tuple_in):
    if not isinstance(tuple_in, tuple):
        print('Ошибка. На входе не кортеж')
        return False
    for i in tuple_in:
        if not isinstance(i, (int, float)):
            print('Ошибка. В кортеже находится не число')
            return False
    return True


def summing_even_numbers(tuple_in):
    validate_result = validate_enter_data(tuple_in)
    if validate_result:
        print(f'Для кортежа чисел: {tuple_in} Сумма четных элементов равна:', end='')
        print(summing_even(tuple_in), '\n')
    else:
        print(f'Ошибка, в кортеже: {tuple_in} Входные данные не верны\n')


test_lists = [(77, 25, 66, 123), (3, 67, 34, 78), 45,
              (64, 29, 'say', 345), (67, 35, 11, 112), (42, 96, 47, 134), (345, 653), (93, 475, 322)]
for index in test_lists:
    summing_even_numbers(index)
    sleep(2)
