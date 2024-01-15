"""
Задание 1:
Напишите программу, которая вычисляет наибольший общий делитель двух целых чисел. На
входе программа принимает два числа.
"""


def finding_divisors(number: int):
    divisors_list = []
    for divisor in range(1, number + 1):
        if number % divisor == 0:
            divisors_list.append(divisor)
    return divisors_list


def find_max_common_item(list1: list, list2: list):
    common_items_list = [x for x in list1 if x in list2]
    return max(common_items_list)


def validation_data(first_number, second_number):
    if ((type(first_number)) != int or (type(second_number)) != int or
            first_number < 1 or second_number < 1):
        print('Входные данные не верны')
        return False  # Введены неверные данные. Ошибка.
    else:
        return True   # Данные верны. Ошибок нет.


def find_max_common_divisor(first_number, second_number):
    # Если данные введены верно, то на выходе наибольший общий делитель.
    # Если данные введены неверно, то на выходе 0.
    if validation_data(first_number, second_number):
        prime_multipliers_list1 = finding_divisors(first_number)
        prime_multipliers_list2 = finding_divisors(second_number)
        max_common_multiplier = find_max_common_item(prime_multipliers_list1, prime_multipliers_list2)
        return max_common_multiplier
    else:
        return 'Входные данные не верны. Общего делителя нет'


# Тестовые прогоны
from random import randint
from time import sleep
test_arguments = [25, 5, 14.3, 28, -1, 20, 'd', 6, 25, 0, 5, 2, 3, 2, 34, 16, 100, 50, 25, 75, 12, 18, 24, 30, 36]
test_len = len(test_arguments)-1
while True:
    item_1 = test_arguments[randint(0, test_len)]
    item_2 = test_arguments[randint(0, test_len)]
    print(f'Число 1: {item_1},  Число 2: {item_2}')
    print('Наибольший общий делитель:', find_max_common_divisor(item_1, item_2), '\n')
    sleep(3)
