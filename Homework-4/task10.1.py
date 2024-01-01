# Задание 10*:
# Измените программу проверки паролей таким образом, чтобы пароль не мог состоять только
# лишь из букв в верхнем регистре, букв в нижнем регистре, цифр и специальных символов.

chars = '!%@#$^&abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
Uper_Chars = range('A', 'Z') #'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Lower_Chars = 'abcdefghijklnopqrstuvwxyz'
Digit_Chars = '1234567890'
Spec_Chars = '!%@#$^&'
def check_password(Password):                           # проверка на длину пароля и на соотвествие списку chars
    if len(Password) < 8:
        return 'Пароль ненадежный, содержит менее восьми символов'
    if all(x in chars for x in Password):
        return 'Пароль содержит 8 или более символов из списка'
    else:
        return 'Пароль содержит символы не из списка'

def check_chars(String_Chars, Password):               # проверка все ли символы пароля в одном регистре
    return all(x in String_Chars for x in Password)    # True - все символы в одном регистре предложенного списка

Input_Password = input('Введите пароль: ')
print(check_password(Input_Password))                   # проверка на соответствие условиям задичи 8

Test_Uper = check_chars(Uper_Chars, Input_Password)         # все ли в высоком регистре
Test_Lower = check_chars(Lower_Chars, Input_Password)       # все ли в низком регистре
Test_Digit = check_chars(Digit_Chars, Input_Password)       # все ли цифры
Test_Spec = check_chars(Spec_Chars, Input_Password)         # все ли спецсимволы

if Test_Spec or Test_Digit or Test_Uper or Test_Lower:
    print('Пароль ненадежный, состоит из символов одного регистра')
else:
    print('Пароль надежный, состоит из символов разных регистров')
