"""
Задание 7:
Напишите программу, которая принимает на вход словарь и ключ, и выводит на экран
значение, соответствующее этому ключу. Если такого ключа нет в словаре, то программа
должна выводить на экран сообщение "Ключ не найден". Пример ввода и вывода:
Введите словарь: {'a': 1, 'b': 2, 'c': 3}
Введите ключ: b
Значение: 2
"""
from random import randint
from time import sleep

def validate_enter_data(dict_in, key_in):
    if not isinstance(dict_in, dict):
        print('Ошибка. На входе не словарь')
        return False
    if not isinstance(key_in, str):
        print('Ошибка. На входе неверный ключ')
        return False
    return True


def printing_dictionary_value(dict_in, key_in):
    validate_result = validate_enter_data(dict_in, key_in)
    print(f'Введен словарь: {dict_in},  ключ: {key_in}\n')
    if validate_result:
        if key_in in dict_in.keys():
            print(f'В словаре: {dict_in}  , под ключем: {key_in}  находится значение: {dict_in[key_in]}\n ')
        else:
            print('Ключ не найден в словаре\n')
    else:
        print('Введены неверные данные\n')


test_list_of_dict = [{'a': 1, 'b': 2, 'c': 3}, {'a': 25, 'd': 5, 'e': 37}, {'a': 31, 'b': 85, 'c': 46},
                     {'a': 31, 'b': 85, 'c': 46}, 'say', 25]
test_list_of_key = ['a', 'b', 'c', 2, 'd', 'e', 'f']
while True:
    dict_index = randint(0, len(test_list_of_dict))-1
    key_index = randint(0, len(test_list_of_key))-1
    printing_dictionary_value(test_list_of_dict[dict_index], test_list_of_key[key_index])
    sleep(3)