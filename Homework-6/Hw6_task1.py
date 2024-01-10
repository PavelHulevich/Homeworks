"""
Задание 1:
Напишите программу, которая вычисляет наибольший общий делитель двух целых чисел. На
входе программа принимает два числа.
"""


def find_prime_multipliers(number: int):
    prime_multipliers_list = []
    for divider in range(1, number+1):
        if number % divider == 0:
            prime_multipliers_list.append(divider)
    return prime_multipliers_list


def find_max_common_item(list1: list, list2: list):
    common_items_list = [x for x in list1 if x in list2]
    return max(common_items_list)


def find_max_common_multiplier(first_number, second_number):
    if ((type(first_number)) != int or (type(second_number)) != int or
            first_number < 1 or second_number < 1):
        return 0
    prime_multipliers_list1 = find_prime_multipliers(first_number)
    prime_multipliers_list2 = find_prime_multipliers(second_number)
    max_common_multiplier = find_max_common_item(prime_multipliers_list1, prime_multipliers_list2)
    return max_common_multiplier


while True:
    num1 = int(input('Введите первое целое положительное число: '))
    num2 = int(input('Введите второе целое положительное число: '))
    res = find_max_common_multiplier(num1, num2)
    if res != 0:
        break
    print('Введены неправильные аргументы. Повторите ввод.\n')

if res == 1:
    print(f'Общий делитель у чисел {num1} и {num2} отсутствует')
else:
    print(f'Наибольший общий делитель у чисел {num1} и {num2}: {res}')
