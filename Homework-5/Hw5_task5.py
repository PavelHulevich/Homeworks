# Задание 5:
# Напишите программу, которая принимает на вход строку, содержащую число в двоичной
# системе счисления, и выводит его в десятичной, восьмеричной и шестнадцатеричной
# системах счисления, используя форматирование строк. Например, если на вход подана строка
# "101010", то на выходе должна быть строка "Decimal: 42, Octal: 52, Hexadecimal: 2A."
# Программа должна использовать 3 метода форматирования (f-strings, % и format) вывести 3
# отформатированные строки.

binary_string_in = "101010"
decimal_in = int(binary_string_in, 2)   # в целое число по основанию 2

                                        # для %-форматирования двоичный вывод не предусмотрен
print('Decimal: %(point)03d, Octal: %(point)#05o, Hexadecimal: %(point)#04x' % {'point': decimal_in})
print('Decimal: {0:03d}, Octal: 0o{0:03o}, Hexadecimal: 0x{0:02x}, Binary: 0b{0:08b}'.format(decimal_in))
print(f'Decimal: {decimal_in:03d}, Octal: 0o{decimal_in:03o}, Hexadecimal: 0x{decimal_in:02x}, Binary: 0b{decimal_in:08b}')

