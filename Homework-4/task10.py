# Задание 10*:
# Измените программу проверки паролей таким образом, чтобы пароль не мог состоять только
# лишь из букв в верхнем регистре, букв в нижнем регистре, цифр и специальных символов.
###
chars = '!%@#$^&abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
Uper_Chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Lower_Chars = 'abcdefghijklnopqrstuvwxyz'
Digit_Chars = '1234567890'
Spec_Chars = '!%@#$^&'


def check_password(Password):  # проверка на длину пароля и на соотвествие списку chars
    if len(Password) < 8:
        return 'Пароль ненадежный, менее восьми символов'
    for index in Password:
        if index not in chars:
            return 'Пароль ненадежный, не все символы из допустимого списка'
    return 'Пароль соответствует задаче №8'


def check_chars(List_Chars, Password):  # проверка все ли символы пароля в одном регистре
    summ_chars = 0
    for index in Password:
        if index in List_Chars:
            summ_chars += 1
    if summ_chars == len(Password):
        return False  # все символы в одном регистре
    return True  # не все символы в одном регистре


Input_Password = input('Введите пароль: ')
print(check_password(Input_Password))

Test_Uper = check_chars(Uper_Chars, Input_Password)  # все ли в высоком регистре
Test_Lower = check_chars(Lower_Chars, Input_Password)  # все ли в низком регистре
Test_Digit = check_chars(Digit_Chars, Input_Password)  # все ли цифры
Test_Spec = check_chars(Spec_Chars, Input_Password)  # все ли спецсимволы

if Test_Spec and Test_Digit and Test_Uper and Test_Lower:
    print('Пароль состоит из символов разных регистров')
else:
    print('Пароль ненадежный, состоит из символов одного регистров')
