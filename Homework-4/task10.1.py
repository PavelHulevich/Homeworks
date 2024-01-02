# Задание 10*:
# Измените программу проверки паролей таким образом, чтобы пароль не мог состоять только
# лишь из букв в верхнем регистре, букв в нижнем регистре, цифр и специальных символов.

chars = '!%@#$^&abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
upper_chars = range('A', 'Z')     # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_chars = range('a', 'z')    # 'abcdefghijklnopqrstuvwxyz'
digit_chars = range(9)           # '1234567890'
spec_chars = '!%@#$^&'
test_list = (upper_chars, lower_chars, digit_chars, spec_chars)  # список из строк символов разных регистров для теста


def check_password(password):                           # проверка на длину пароля и на соответствие списку chars
    if len(password) < 8:
        return 'Пароль ненадежный, содержит менее восьми символов'
    if all(x in chars for x in password):
        return 'Пароль содержит 8 или более символов из списка'
    else:
        return 'Пароль содержит символы не из списка'


def check_chars(string_chars, password):               # проверка все ли символы пароля в одном регистре предлож. списка
    return all(x in string_chars for x in password)    # True - все символы в одном регистре предложенного списка


Input_Password = input('Введите пароль: ')
print(check_password(Input_Password))                   # проверка на длину пароля и на соответствие списку chars
test = True
for test_chars in test_list:                        # перебираем список тестовых строк (с символами разных регистров)
    test = test and check_chars(test_chars, input_password)  # проверка все ли символы пароля в одном регистр
if test:
    print('Пароль состоит из символов разных регистров')
else:
    print('Пароль ненадежный, состоит из символов одного регистров')
