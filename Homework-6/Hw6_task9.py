"""
Задание 9:
Напишите программу, которая найдет самую длинную строку с общим префиксом среди
массива строк. Если общего префикса нет, верните пустую строку.
Пример: если на вход подан список ["flower","flow","flight"], то на выходе должна быть
строка "fl". Если подан список ["dog","racecar","car"], то на выходе должна быть строка "".
"""


def find_common_prefix(list_in):
    # Поиск общего префикса. На выходе строка с общим префиксом или "" если нет общего префикса.
    word_min_len = min((len(i) for i in list_in))
    common_prefix = ''
    for index_of_char in range(0, word_min_len):
        common_prefix += list_in[0][index_of_char]
        is_diff_char = False
        for word in list_in:
            if word[index_of_char] != common_prefix[index_of_char]:
                is_diff_char = True
                break
        if is_diff_char:
            common_prefix = common_prefix[0:-1]
            break
    return common_prefix


def checking_input_data(list_in):
    # Проверка валидности исходных данных. На выходе либо код ошибки, либо 0, если нет ошибки.
    if not isinstance(list_in, list):
        print('Ошибка. На входе не список')
        return 'Ошибка. Нет общего префикса'
    for i in list_in:
        if not isinstance(i, str):
            print("Ошибка. Список содержит не строки")
            return 'Ошибка. Нет общего префикса'
    return 0  # No errors


def find_same_begin_entrance(list_in):
    # Проверяем валидность входных данных. Если данные не соответствуют - передаем на выход код ошибки
    # Иначе - На выходе список с общим для всех элементов списка префиксом, либо "" если общего префикса нет.
    check_input = checking_input_data(list_in)
    if check_input != 0:
        return check_input
    else:
        return find_common_prefix(list_in)


# Тестовые прогоны
test_lists = (["flower", "flow", "flight"], ["flower", "flow", "floor"], 25,
              'beer', ["flower", 25, "flight"], ["flower", [100, 5], "flight"])
for x in test_lists:
    print(f'В списке слов: {x}, общий префикс: ', find_same_begin_entrance(x), '\n')
