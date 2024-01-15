"""
Задание 15:
Напишите программу, которая использует генератор множества для создания множества,
которое состоит из всех делителей заданного числа n. Делители числа - это числа, на которые
это число делится без остатка. Программа должна принимать на вход число n и выводить на
экран полученное множество. Пример ввода и вывода:
Введите число: 12
Множество делителей: {1, 2, 3, 4, 6, 12}
"""
from random import randint
from time import sleep


def finding_divisors_set(number: int) -> set:
    divisors_set = set()
    divisors = range(1, int(number/2) + 1)  # Ищем делители только до половины числа. Следующий делитель - само число.
    for divisor in divisors:
        if number % divisor == 0:
            divisors_set.add(divisor)
    divisors_set.add(number)  # В конец множества просто добавляем само входное число, как последний делитель.
    return divisors_set


def validate_enter_data(number: int) -> bool:
    # Проверка валидности исходных данных. На выходе False - если ошибка входных данных.
    if not isinstance(number, int):
        print('Ошибка. На входе не целое число')
        return False
    if number == 0:
        print('Ошибка. На входе ноль')
        return False

    return True  # No errors


def finding_divisors_set_entrance(number: int):
    validate_result = validate_enter_data(number)
    if validate_result:
        print(f'Число: {number} имеет делители : {finding_divisors_set(number)}\n')
    else:
        print(f'Ошибка, в аргументе: "{number}" входные данные не верны\n')


# Тестовые прогоны
tests_list = [12, 36, 48, '65', 75, 'stay', 2, 47, 36, [852, 67, 49], 23, 45, [69, 78, 578], 0, 49, '75', 45, 65, 78]

while True:
    test_index = randint(0, len(tests_list)-1)
    finding_divisors_set_entrance(tests_list[test_index])
    sleep(3)
