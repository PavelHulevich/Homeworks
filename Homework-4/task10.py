# Задание 10*:
# Измените программу проверки паролей таким образом, чтобы пароль не мог состоять только
# лишь из букв в верхнем регистре, букв в нижнем регистре, цифр и специальных символов.
###
# chars = '!%@#$^&abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
upper_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_chars = 'abcdefghijklnopqrstuvwxyz'
digit_chars = '1234567890'
spec_chars = '!%@#$^&'
test_list = (upper_chars, lower_chars, digit_chars, spec_chars)  # список из строк символов разных регистров для теста


def check_password(password):            # проверка на длину пароля и на соответствие списку chars
    if len(password) < 8:
        return 'Пароль ненадежный, менее восьми символов'
    for index in password:
        if index not in ''.join(test_list):
            return 'Пароль ненадежный, не все символы из допустимого списка'
    return 'Пароль соответствует задаче №8'


def check_chars(list_chars, password):  # проверка все ли символы пароля в одном регистре
    summ_chars = 0
    for index in password:
        if index in list_chars:
            summ_chars += 1
    if summ_chars == len(password):
        return False                    # все символы в одном регистре
    return True                         # не все символы в одном регистре


input_password = input('Введите пароль: ')
print(check_password(input_password))   # проверка на длину пароля и на соответствие списку chars

test = True
for test_chars in test_list:            # перебираем список тестовых строк (с символами разных регистров)
    test = test and check_chars(test_chars, input_password)  # проверка все ли символы пароля в одном регистр
if test:
    print('Пароль состоит из символов разных регистров')
else:
    print('Пароль ненадежный, состоит из символов одного регистров')
