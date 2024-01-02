# Задание 6:
# Написать 2 программы для шифрования и дешифрования сообщений шифром Цезаря. Шаг
# шифровки и исходное сообщение задается пользователем вручную.
# Алфавит 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# Шифр Цезаря - это простой тип подстановочного шифра, где каждая буква обычного текста
# заменяется буквой с фиксированным числом позиций вниз по алфавиту

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # 26 символов


def coding_string(string, step):  # Шифрование
    string_out = ''
    for char in string:         # перебираем все символы во введенной строке
        if char == ' ':         # если символ ' ' то оставляем пробел в том же месте
            string_out += ' '       # |
        else:
            char_index = alphabet.find(char)    # индекс текущего символа в алфавите
            char_index += step                  # индекс символа меняется на шаг кодирования
            if char_index > 25:                 # контроль выхода индекса за границы алфавита
                char_index -= 26                    # |
            elif char_index < 0:                    # |
                char_index += 26                    # |
            string_out += alphabet[char_index]  # Выходная строка формируется
    return string_out


def decoding_string(string, step):  # Дешифрование
    string_out = ''
    for char in string:  # перебираем все символы во введенной строке
        if char == ' ':  # если символ ' ' то оставляем пробел в том же месте
            string_out += ' '  # |
        else:
            char_index = alphabet.find(char)  # индекс текущего символа в алфавите
            char_index -= step  # индекс символа меняется на шаг обратный шагу кодирования
            if char_index > 25:  # контроль выхода индекса за границы алфавита
                char_index -= 26  # |
            elif char_index < 0:  # |
                char_index += 26  # |
            string_out += alphabet[char_index]  # Выходная строка формируется
    return string_out


string_in = 'TEST MESSAGE'  # сообщение для шифрования
step_in = -3                # шаг шифрования
code_string_out = coding_string(string_in, step_in)
decode_string_out = decoding_string(code_string_out, step_in)

print(f'Сообщение для шифрования:      {string_in}')
print(f'Сообщения после шифрования:    {code_string_out}')
print(f'Сообщение после дешифрования:  {decode_string_out}')
