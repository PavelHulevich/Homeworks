# Задание 2:
# Напишите программу для разворачивания строк в списке ["apple", "banana", "cherry"]
# используя функцию map. Программа должна вывести каждый тапл на новой строке.

def reverse_string(string):                               # функция реверса любой строки
    return string[::-1]


list_of_strings = ["apple", "banana", "cherry"]
map_of_rev_strings = map(reverse_string, list_of_strings)  # реверс всех строк списка и запись их в мап-список строк
for i in map_of_rev_strings:                               # вывод на печать перевернутых строк из мап-списка строк
    print(i)
