# Задание 1:
# Напишите программу, объединяющую 3 списка в список tuple-ов
# используя функцию zip.
# Программа должна вывести каждый тапл на новой строке.
# Списки для объединения:
# ["a", "b", "c"]
# [1, 2, 3]
# ["%", "$", "@"]

first_list = ["a", "b", "c"]
second_list = [1, 2, 3]
third_list = ["%", "$", "@"]

zip_of_tuples = zip(first_list, second_list, third_list)  # все списки в зип таплов

for index in zip_of_tuples:
    print("содержимое класса zip c таплами: ", index)
