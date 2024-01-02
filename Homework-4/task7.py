# Задание 7:
# Реализуйте функцию, генерирующую пароль используя генератор. Для пароля разрешено
# использовать символы из списка chars = '+-/*!&$#?
# =@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
# Чтобы извлечь уникальный символ, воспользуйтесь методом random.choice(chars).
# Функция принимает в качестве аргумента длину пароля и возвращает строку с паролем.

import random


def pass_generator(pass_length):
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password = ''
    for _ in range(pass_length):
        password += random.choice(chars)
    return password


print(pass_generator(11))
