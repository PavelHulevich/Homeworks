# Задание 7:
# Реализуйте функцию, генерирующую пароль используя генератор. Для пароля разрешено
# использовать символы из списка chars = '+-/*!&$#?
# =@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
# Чтобы извлечь уникальный символ воспользуйтесь методом random.choice(chars).
# Функция принимает в качестве аргумента длинну пароля и возвращает строку с паролем.

import random
def pass_generator(Pass_Length):
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    Password = ''
    for index in range(Pass_Length):                # первый вариант цикла
        Password = Password + random.choice(chars)
    return Password

# def pass_generator(Pass_Length):
#     chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
#     Password = ''
#     index = 1
#     while index <= Pass_Length:                   # второй вариант цикла
#         index = index+1
#         Password = Password + random.choice(chars)
#     return Password

print(pass_generator(11))



