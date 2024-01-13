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


def validation_data(first_number, second_number):
    # Checking data validity
    if ((type(first_number)) != int or (type(second_number)) != int or
            first_number < 1 or second_number < 1):
        print('Входные данные не верны')
        return False  # Введены неверные данные. Ошибка.
    else:
        return True   # Данные верны. Ошибок нет.


def find_max_common_multiplier(first_number, second_number):
    # Если данные введены верно, то на выходе наибольший общий делитель.
    # Если данные введены неверно, то на выходе 0.
    if validation_data(first_number, second_number):
        prime_multipliers_list1 = find_prime_multipliers(first_number)
        prime_multipliers_list2 = find_prime_multipliers(second_number)
        max_common_multiplier = find_max_common_item(prime_multipliers_list1, prime_multipliers_list2)
        return max_common_multiplier
    else:
        return 0


# Test example
test_arguments = [[25, 5], [14.3, 28], [-1, 20], ['d', 6], [25, 0], [[5, 2, 3], 2]]
for i in test_arguments:
    print(f'Число 1: {i[0]},  Число 2: {i[1]}')
    print('Наибольший общий делитель:', find_max_common_multiplier(i[0], i[1]), '\n')
