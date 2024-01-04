# Задание 10*:
# Измените программу проверки паролей таким образом, чтобы пароль не мог состоять только
# лишь из букв в верхнем регистре, букв в нижнем регистре, цифр и специальных символов.

chars = '!%@#$^&abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
upper_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_chars = 'abcdefghijklnopqrstuvwxyz'
digit_chars = '1234567890'
spec_chars = '!%@#$^&'
test_list = (upper_chars, lower_chars, digit_chars, spec_chars)  # список из строк символов разных регистров для теста


def is_password_safe(password):                           # проверка на длину пароля и на соответствие списку chars
    return len(password) >= 8 and all(x in chars for x in password)  # True если пароль подходит


def is_password_in_set(string_chars, password):
    return not all(x in string_chars for x in password)
#   return any(x in string_chars for x in password) <==Заменить на строку что бы пароль имел символы из всех 4-х списков


def is_password_diff_charset(password):
    password_diff_charset = True
    for test_chars in test_list:  # перебираем список тестовых строк (с символами в разных регистрах)
        password_diff_charset = password_diff_charset and is_password_in_set(test_chars, password)
    return password_diff_charset


input_password = input('Введите пароль: ')
if is_password_safe(input_password) and is_password_diff_charset(input_password):
    print('Пароль надежный')
else:
    print('Пароль ненадежный')
