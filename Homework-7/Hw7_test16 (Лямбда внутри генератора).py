"""
Задание 16:
Напишите программу, которая использует генератор множества для создания множества,
которое состоит из всех букв алфавита от "a" до "z", которые не входят в некоторую строку.
Программа должна выводить на экран полученное множество. Программа должна
использовать лямбда-функцию для создания списка букв алфавита.
Пример вывода для строки "Hello, world!":
Множество букв, которые не входят в строку: {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'n', 'p', 'q', 's', 't', 'u',
'v', 'x', 'y', 'z'}
"""
from random import randint
from time import sleep


def validate_enter_data(string: str) -> bool:
    # Проверка валидности исходных данных. На выходе False - если ошибка входных данных.
    if not isinstance(string, str):
        print('Ошибка. На входе не строка')
        return False
    return True  # No errors


def finding_different_set_enter(string: str):
    validate_result = validate_enter_data(string)
    if validate_result:
        alphabet_out = lambda string_in: {chr(i) for i in range(97, 123) if chr(i) not in string_in}
        print(f'Введена строка: "{string}"\n'
              f'множество символов алфавита за минусом входящих в строку: {alphabet_out(string)} \n')
    else:
        print(f'Ошибка, в аргументе: "{string}" входные данные не верны (не строка)\n')


# Тестовые прогоны
tests_list = ["Hello, world!",  "vending machine", 'drinks', 25, ['machine', 'vending'], {25, 35, 75}, 'a']
while True:
    test_index = randint(0, len(tests_list)-1)
    finding_different_set_enter(tests_list[test_index])
    sleep(3)
