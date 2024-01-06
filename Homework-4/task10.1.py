# Задание 10*:
# Измените программу проверки паролей таким образом, чтобы пароль не мог состоять только
# лишь из букв в верхнем регистре, букв в нижнем регистре, цифр и специальных символов.

chars = '!%@#$^&abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
upper_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_chars = 'abcdefghijklnopqrstuvwxyz'
digit_chars = '1234567890'
spec_chars = '!%@#$^&'
test_list = (upper_chars, lower_chars, digit_chars, spec_chars)  # список из строк символов разных регистров для теста

input_password = 'Aa1!'

is_pass_safe = True  #
for test_chars in test_list:                                        # итерируемся по списку тестовых наборов
    is_pass_safe *= any(x in test_chars for x in input_password)    # хотя бы один символ пароля входит в тест. набор
if is_pass_safe:
    print('Пароль содержит символы из разных четырех наборов символов')
else:
    print('ПАРОЛЬ НЕ СОДЕРЖИТ СИМВОЛЫ ИЗ РАЗНЫХ ЧЕТЫРЕХ НАБОРОВ СИМВОЛОВ')

# is_pass_safe = True
# for test_chars in test_list:
#     is_pass_safe *= not all(x in test_chars for x in input_password)
# if is_pass_safe:
#     print('Пароль не содержит символы только из одного набора символов')
# else:
#     print('ПАРОЛЬ СОДЕРЖИТ СИМВОЛЫ ТОЛЬКО ИЗ ОДНОГО НАБОРА СИМВОЛОВ')


