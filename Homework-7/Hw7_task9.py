'''
Задание 9:
Напишите программу, которая принимает на вход два множества и выводит на экран их
объединение, пересечение, разность и симметричную разность. Программа должна
использовать операторы |, &, -, ^ для работы с множествами. Пример ввода и вывода:
Введите первое множество: {1, 2, 3, 4}
Введите второе множество: {3, 4, 5, 6}
Объединение: {1, 2, 3, 4, 5, 6}
Пересечение: {3, 4}
Разность: {1, 2}
Симметричная разность: {1, 2, 5, 6}
'''
from random import randint
from time import sleep


def operating_with_sets(set_in_1, set_in_2):
    print(f'Введены множества:   {set_in_1}   и:   {set_in_2}\nРезультаы операций с множествами:  ')
    print('Объединение      :  ', set_in_1 | set_in_2)
    print('Пересечение      :  ', set_in_1 & set_in_2)
    print('Разность         :  ', set_in_1 - set_in_2)
    print('Симметр. разность:  ', set_in_1 ^ set_in_2)
    print()


def validate_enter_data(set_1, set_2):
    if not isinstance(set_1, set) or not isinstance(set_2, set):
        print('Ошибка. На входе не множество')
        return False
    return True


def operating_with_sets_enter(set_1, set_2):
    validate_result = validate_enter_data(set_1, set_2)
    if validate_result:
        operating_with_sets(set_1, set_2)
        return True  # No errors
    else:
        print(f'Введены неверные данные: {set_1},   {set_2}\n')
        return False  # Errors


test_sets = ({1, 2, 3, 4}, {3, 4, 5, 6}, {71, 25, 3, 4}, {3, 4, 28, 6}, {1, 45, 3, 4},
             {3, 4, 'say', 6}, {1, 'in', 3, 4}, {3, 4, 5, 6}, 'day', 25)
while True:
    set_index_1 = randint(0, len(test_sets)) - 1
    set_index_2 = randint(0, len(test_sets)) - 1
    operating_with_sets_enter(test_sets[set_index_1], test_sets[set_index_2])
    sleep(3)
