"""
Задание 12:
Напишите программу, которая использует генератор словаря для создания словаря, в котором
ключи - это числа от 1 до 10, а значения - это списки, которые состоят из делителей этих
чисел. Делители числа - это числа, на которые это число делится без остатка. Программа
должна выводить на экран полученный словарь. Пример вывода:
{1: [1], 2: [1, 2], 3: [1, 3], 4: [1, 2, 4], 5: [1, 5], 6: [1, 2, 3, 6], 7: [1, 7], 8: [1, 2, 4, 8], 9: [1, 3, 9], 10:
[1, 2, 5, 10]}
"""
from time import time

# def finding_divisors_slow(number: int):
#     divisors_list = []
#     for divisor in range(1, number + 1):
#         if number % divisor == 0:
#             divisors_list.append(divisor)
#     return divisors_list
def finding_divisors_fast(number: int):
    divisors_list = []
    divisors = range(1, int(number/2) + 1)  # Ищем делители только до половины числа. Следующий делитель - само число.
    for divisor in divisors:
        if number % divisor == 0:
            divisors_list.append(divisor)
    divisors_list.append(number)  # В конец списка просто добавляем само число, как последний делитель.
    return divisors_list


# Вычисление словаря с делителями ключей
dict_1 = {}
dict_size = (range(1, 11))
timer_size = range(100000)
print('\nВычисление делителей')
start_fn1 = time()
for _ in timer_size:
    for i in dict_size:
        dict_1[i] = finding_divisors_fast(i)
stop_fn1 = time()
print(dict_1)
print(f'Вычисление 1 млн словарей потребует: {(stop_fn1 - start_fn1) * 10:0.2f} секунд машинного времени\n')
