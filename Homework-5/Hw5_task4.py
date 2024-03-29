# Задание 4:
# Напишите программу, которая принимает на вход строку, содержащую название книги,
# автора и год издания, и выводит ее в другом формате. Например, если на вход подана строка
# "Война и мир, Лев Толстой, 1869", то на выходе должна быть строка "Толстой, Лев. Война и
# мир. 1869." Программа должна использовать 3 метода форматирования (f-strings, % и format)
# вывести 3 отформатированные строки.

def print_formatted_text(string):
    string_list = string.split(' ')
    print(f'{string_list[4]} {string_list[3]}. {" ".join(string_list[:3])[:-1]}. {string_list[5]}.')
    print('%s %s. %s. %s.' % (string_list[4], string_list[3], " ".join(string_list[:3])[:-1], string_list[5]))
    print('{} {}. {}. {}.'.format(string_list[4], string_list[3], " ".join(string_list[:3])[:-1], string_list[5]))


string_in = 'Война и мир, Лев Толстой, 1869'
print_formatted_text(string_in)