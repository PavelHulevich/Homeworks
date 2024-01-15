"""
Задание 11:
Напишите программу, которая использует генератор словаря для создания словаря, в котором
ключи - это числа от 1 до 10, а значения - это факториалы этих чисел. Факториал числа - это
произведение всех натуральных чисел от 1 до этого числа. Программа должна выводить на
экран полученный словарь. Пример вывода:
{1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880, 10: 3628800}
"""

from math import factorial
from time import time

# Вычисление факториала используя math.factorial().
dict_1 = {}
dict_size = (range(1, 11))
timer_size = range(100000)
print('\nВычисление факториала используя math.factorial()')
start_fn1 = time()
for _ in timer_size:
    for i in dict_size:
        dict_1[i] = factorial(i)
stop_fn1 = time()
print(dict_1)
print(f'Вычисление 1 млн словарей потребует: {(stop_fn1 - start_fn1) * 10:0.2f} секунд машинного времени\n')


# Вычисление факториала используя функцию пользователя.
def calculating_factorial(number):
    fact_out = 1
    for j in range(1, number + 1):
        fact_out = fact_out * j
    return fact_out


print('Вычисление факториала используя функцию пользователя')
start_fn2 = time()
for _ in timer_size:
    for i in dict_size:
        dict_1[i] = calculating_factorial(i)
stop_fn2 = time()
print(dict_1)
print(f'Вычисление 1 млн словарей потребует: {(stop_fn2 - start_fn2) * 10:0.2f} секунд машинного времени\n')
