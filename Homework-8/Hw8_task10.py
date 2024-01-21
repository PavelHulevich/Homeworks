"""Задание 10*:
Напишите генератор, который возвращает все подмножества данного множества.
Подмножество - это множество, которое содержит только те элементы, которые есть в
исходном множестве. Например, подмножествами множества {1, 2, 3} являются {}, {1}, {2},
{3}, {1, 2}, {1, 3}, {2, 3} и {1, 2, 3}."""
from random import choice
from time import sleep


def finding_subsets(set_in: set) -> list:
    list_in = list(set_in)
    list_in_len = len(list_in)
    list_of_lists_out = []
    for item in range(0, int(2 ** list_in_len)):
        list_current = []
        bit_current = 0
        item_bin = bin(item)
        while item_bin[-1] != 'b':
            last_bit = int(item_bin[-1])
            if last_bit == 1:
                list_current.append(list_in[bit_current])
            item_bin = item_bin[:-1]
            bit_current += 1
        list_of_lists_out.append(set(list_current))
    return [list_of_lists_out]


def validate_enter_data(set_in: set) -> bool:
    if not isinstance(set_in, set):
        print('Ошибка. На входе не множество')
        return False
    for i in set_in:
        if not isinstance(i, int):
            print('Ошибка. В множестве не целые числа.')
            return False
    return True


def finding_subsets_entry(set_in: set) -> None:
    validate_result = validate_enter_data(set_in)
    print('Введено множество :', set_in)
    if validate_result:
        list_of_sets = finding_subsets(set_in)
        print(f'Все возможные подмножества составляют: \n{list_of_sets}\n')
    else:
        print('На входе неверные данные\n')


TEST_LIST = [{1, 2, 3, 4, 5}, {1, 2, 3, 4}, {1, 2, 3}, {1, 2, 'S', 4, 5},
                  [1, 2, 3, 4, 5], 25, 'day', {1, 2, 3, 4.45, 5},
                  {1, 2}, {1, 2, 3}, {1, 2, 3}, {1, 2, 'say', 4, 5},]
while True:
    finding_subsets_entry(choice(TEST_LIST))
    sleep(3)
