'''
Задание 10:
Напишите программу, которая принимает на вход два множества и проверяет, является ли
одно множество подмножеством другого. Программа должна выводить на экран "Да", если
одно множество является подмножеством другого, и "Нет" в противном случае. Пример
ввода и вывода:
Введите первое множество: {1, 2, 3}
Введите второе множество: {1, 2, 3, 4, 5}
Да
'''
from random import randint
from time import sleep


def is_set_subset(set_1, set_2):
    is_subset = True
    if set_1 - set_2 == set():
        print(f'Множество  {set_1}  ЯВЛЯЕТСЯ подмножеством  {set_2}\n')
    elif set_2 - set_1 == set():
        print(f'Множество  {set_2}  ЯВЛЯЕТСЯ подмножеством  {set_1}\n')
    else:
        print(f'Множества  {set_1}  и  {set_2}  не являются подмножествами друг другу\n ')
        is_subset = False
    return is_subset


def validate_enter_data(set_1, set_2):
    if not isinstance(set_1, set) or not isinstance(set_2, set):
        print('Ошибка. На входе не множество')
        return False
    return True


def operating_with_sets_enter(set_1, set_2):
    validate_result = validate_enter_data(set_1, set_2)
    if validate_result:
        is_set_subset(set_1, set_2)
        return True  # No errors
    else:
        print(f'Введены неверные данные: {set_1},   {set_2}\n')
        return False  # Errors

# Тестовые прогоны
test_sets = ({1, 2, 3}, {1, 2, 3, 4, 5}, {1, 2, 3, 4, 5, 10}, {1, 2, 3, 4}, {71, 25, 3, 4}, {3, 4, 28, 6},
             {1, 2, 3, 4, 8}, {1, 2, 3}, {1, 2, 3}, {1, 2, 3},
             {1, 2, 3, 4}, {1, 'in', 3, 4}, {3, 4, 5, 6}, 'day', 25)
while True:
    set_index_1 = randint(0, len(test_sets)) - 1
    set_index_2 = randint(0, len(test_sets)) - 1
    operating_with_sets_enter(test_sets[set_index_1], test_sets[set_index_2])
    sleep(3)

