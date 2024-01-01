# Задание 2:
# Напишите программу для разворачивания строк в списке ["apple", "banana", "cherry"]
# используя функцию map. Программа должна вывести каждый тапл на новой строке.

def reverse_string(string):                               #функция реверса любой строки
    return string[::-1]

List_of_Strings = ["apple", "banana", "cherry"]
Map_of_RevStrings = map(reverse_string, List_of_Strings)  #реверс всех строк списка и запись их в мап строк

for index in Map_of_RevStrings:                           #вывод на печать перевернутых строк из мап строк
    print(index)


