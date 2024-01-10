"""
Задание 3:
Напишите программу, которая принимает на вход список чисел и выводит на экран
максимальное и минимальное число в списке. Программа не должна использовать
встроенные функции max и min для поиска максимума и минимума.
"""
number_list = [34, 87, 5.3, 475, 56, 765, 321,]
for i in number_list:
    if (type(i)) != int and (type(i)) != float:
        print('В списке находится не число')
        exit()

# Way-1. Simplest
number_list.sort()
print(number_list[0], number_list[-1])

# Way-2. For-Cycle
max_num = number_list[0]
min_num = number_list[0]
for i in number_list:
    if i < min_num:
        min_num = i
    if i > max_num:
        max_num = i
print(min_num, max_num)

# Way-3. While-Cycle
max_num = number_list[0]
min_num = number_list[0]
i = 0
while i < len(number_list):
    if number_list[i] < min_num:
        min_num = number_list[1]
    if number_list[i] > max_num:
        max_num = number_list[i]
    i += 1
print(min_num, max_num)