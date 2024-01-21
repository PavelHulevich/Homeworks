"""
Задание 1:
Напишите генератор, который принимает число n и возвращает сумму квадратов всех чисел
от 1 до n.
"""

from random import choice
from time import sleep


def validate_enter_data(number: int) -> bool:
    # Проверка валидности исходных данных. На выходе False - если ошибка входных данных.
    if not isinstance(number, int):
        print('Ошибка. На входе не целое число')
        return False
    return True  # No errors


def summ_of_squares_enter(number: int):
    validate_result = validate_enter_data(number)
    if validate_result:
        summ_of_squares = lambda n: sum([i**2 for i in range(1, n+1)])
        print(f'Введено число: {number}\n'
              f'сумма квадратов всех чисел от 1 до {number} = {summ_of_squares(number )} \n')
    else:
        print(f'Ошибка, в аргументе: "{number}" входные данные не верны\n')


# Тестовые прогоны
TESTS_LIST = ["Hello, world!",  2, 3, 6, 5, 25, 4, ['machine', 'vending'], {25, 35, 75}, 'a']
while True:
    summ_of_squares_enter(choice(TESTS_LIST))
    sleep(2)
