# Задание 2:
# Напишите программу, которая принимает на вход строку, содержащую несколько слов,
# разделенных пробелами, и выводит ее в обратном порядке, используя форматирование строк.
# Например, если на вход подана строка "Hello World", то на выходе должна быть строка
# "World Hello". Нельзя использовать циклы. Программа должна использовать 3 метода
# форматирования (f-strings, % и format) вывести 3 отформатированные строки.


def print_reverse_string_1(string):
    # Вариант для строки с любым количеством слов
    strings_list = string.split(' ')                  # Список слов из введенной строки
    strings_list = strings_list[::-1]                  # Реверс списка слов
    string_out = ' '.join(strings_list)               # Строка из реверсного списка слов
    print(f'{string_out}')
    print('%s' % string_out)
    print('{0}\n'.format(string_out))


def print_reverse_string_2(string):
    # Вариант для строки с известным количеством слов (два слова)
    string_list = string.split(' ')                   # Список слов из введенной строки
    print(f'{string_list[1]} {string_list[0]}')
    print('%s %s' % (string_list[1], string_list[0]))
    print('{1} {0}'.format(string_list[0], string_list[1]))


string_in = 'Hello World'
print_reverse_string_1(string_in)
print_reverse_string_2(string_in)
