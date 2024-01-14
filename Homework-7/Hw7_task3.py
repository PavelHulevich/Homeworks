"""
Задание 3:
Напишите программу, которая принимает на вход список слов и выводит на экран кортеж,
который состоит из самого длинного и самого короткого слова в списке. Программа должна
учитывать регистр букв и не использовать встроенные функции len, max и min для работы со
строками.
"""
from time import sleep


def find_short_long(list_in):
    def find_word_length(word):
        word_length = 0
        for _ in word:
            word_length += 1
        return word_length

    min_max_words = [list_in[0], list_in[0]]
    for word in list_in:
        word_len = find_word_length(word)
        if word_len < find_word_length(min_max_words[0]):
            min_max_words[0] = word
        if word_len > find_word_length(min_max_words[1]):
            min_max_words[1] = word
    return tuple(min_max_words)


def validate_enter_data(list_in):
    # Проверка валидности исходных данных. На выходе False - если ошибка входных данных.
    if not isinstance(list_in, list):
        print('Ошибка. На входе не список')
        return False
    for i in list_in:
        if not isinstance(i, str):
            print("Ошибка. Список содержит не строку")
            return False
    return True  # No errors


def find_short_long_words(list_in):
    validate_result = validate_enter_data(list_in)
    if validate_result:
        print(f'В списке слов: {list_in}  самое короткое и самое длинное слово:  ', end='')
        print(find_short_long(list_in), '\n')
    else:
        print(f'Ошибка, в списке {list_in} входные данные не верны\n')


test_lists = [['Программа', 'должна', 'учитывать', 'регистр', 'букв'], ['принимает', 'на', 'вход', 'список', 'слов'],
              ['использовать', 'встроенные', 'функции'], ['который', 'состоит', 'из', 'самого', 'длинного'],
              ['который', 25, 'из', 'самого', 'длинного'], 75,  ('который', 'состоит', 'из', 'самого', 'длинного')]
for index in test_lists:
    find_short_long_words(index)
    sleep(3)
