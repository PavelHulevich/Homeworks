# Задание 10*:
# Измените программу проверки паролей таким образом, чтобы пароль не мог состоять только
# лишь из букв в верхнем регистре, букв в нижнем регистре, цифр и специальных символов.

chars = '!%@#$^&abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
upper_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_chars = 'abcdefghijklnopqrstuvwxyz'
digit_chars = '1234567890'
spec_chars = '!%@#$^&'
test_list = (upper_chars, lower_chars, digit_chars, spec_chars)  # список из строк символов разных регистров для теста


def check_password(password):                           # проверка на длину пароля и на соответствие списку chars
    return len(password) >= 8 and all(x in chars for x in password)  # True если пароль подходит


def check_chars(string_chars, password):               # проверка все ли символы пароля в одном регистре предлож. списка
    return not all(x in string_chars for x in password)    # True - не все символы в одном регистре предложенного списка
#   return any(x in string_chars for x in password) <==Заменить на строку что бы пароль имел символы из всех 4-х списков


input_password = input('Введите пароль: ')
test = (check_password(input_password))             # проверка на длину пароля и на соответствие списку chars
for test_chars in test_list:                        # перебираем список тестовых строк (с символами в разных регистрах)
    test = test and check_chars(test_chars, input_password)  # проверка все ли символы пароля в одном регистре
if test:
    print('Пароль надежный')
else:
    print('Пароль ненадежный')
