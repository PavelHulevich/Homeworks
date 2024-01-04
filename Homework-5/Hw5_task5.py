# Задание 5:
# Напишите программу, которая принимает на вход строку, содержащую число в двоичной
# системе счисления, и выводит его в десятичной, восьмеричной и шестнадцатеричной
# системах счисления, используя форматирование строк. Например, если на вход подана строка
# "101010", то на выходе должна быть строка "Decimal: 42, Octal: 52, Hexadecimal: 2A."
# Программа должна использовать 3 метода форматирования (f-strings, % и format) вывести 3
# отформатированные строки.

def print_formatted_number(number):
    print('Decimal: %(point)03d, Octal: %(point)#05o, Hexadecimal: %(point)#04x' % {'point': number})
    print('Decimal: {0:03d}, Octal: 0o{0:03o}, Hexadecimal: 0x{0:02x}, Binary: 0b{0:08b}'.format(number))
    print(f'Decimal: {number:03d}, Octal: 0o{number:03o}, Hexadecimal: 0x{number:02x}, '
          f'Binary: 0b{number:08b}')


binary_string_in = "101010"
decimal_in = int(binary_string_in, 2)   # в целое число по основанию 2
print_formatted_number(decimal_in)
