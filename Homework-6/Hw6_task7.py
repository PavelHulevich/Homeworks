"""
Задание 7:
Написать программу, которая определяет количество учеников в классе, чей рост превышает
средний. На входе программа принимает список чисел.
"""


def counting_above_average(list_of_height):
    average_height = sum(list_of_height) / len(list_of_height)
    above_average = 0
    for height in list_of_height:
        if height > average_height:
            above_average += 1
    return above_average


def checking_input_data(list_of_height):
    if not isinstance(list_of_height, list):
        print('Ошибка. На входе не список')
        return 'Ошибка входных данных'
    for i in list_of_height:
        if not isinstance(i, (int, float)):
            print('Ошибка. В элементах списка содержится не число')
            return 'Ошибка входных данных'
    return 0


def counting_above_average_entrance(list_of_height):    # Точка входа в выполнение задания
    check_result = checking_input_data(list_of_height)  # Функция проверки входных данных
    if check_result != 0:
        return check_result
    else:
        return counting_above_average(list_of_height)   # Основная функция. Считаем учеников с ростом выше среднего.


# Тестовые прогоны
test_lists = [[125, 135, 127, 145, 150, 130, 140, 132], [125, 135, '127', 145, 150, 130, 140, 132], 'say', 25]
for list_in in test_lists:
    print(f'Рост учеников в классе: {list_in}')
    print('Число учеников с ростом выше среднего :', counting_above_average_entrance(list_in), '\n')
