# """Задание 7:
# Напишите функцию modify_list(lst: list, *funcs: callable) -> None, которая принимает в
# качестве аргументов список lst и произвольное количество функций funcs, и модифицирует
# список lst так, что каждый его элемент преобразуется с помощью всех функций из funcs по
# порядку. Функции из funcs должны принимать один аргумент и возвращать одно значение.
# Функция modify_list не должна возвращать ничего, а изменять список lst на месте. Например,
# modify_list([1, 2, 3], lambda x: x + 1, lambda x: x * 2) должна изменить список [1, 2, 3] на [4, 6,
# 8], так как каждый элемент сначала увеличивается на 1, а потом умножается на 2. Функции
# для модификации элеметов списка:
# • Возведение в квадрат четных чисел
# • Увеличение на 1 нечетных чисел
# • Умножение на 3 простых чисел"""
#
#
# def modify_list(a: int, *funcs: callable) -> None:
#     funcs[1](10)
#     funcs[0](10)
#
#
# # def square_of_even(number):
# #     print(1)
# #
# # def increment_of_odd():
# #     print(2)
# #
# # TEST_LIST = [2, 4, 6, 10]
# def test_func(b):
#     print(b*3)
#
#
# def test_func2(b):
#     print(b/2)
#
# modify_list(3, test_func, test_func2)

print(6 % 3)



# def is_validate_data(list_in: list) -> bool:
#     # Проверка валидности исходных данных. На выходе False - если ошибка входных данных.
#     if not isinstance(list_in, list):
#         print('Ошибка. На входе не список')
#         return False
#     for number in list_in:
#         if not isinstance(number, int):
#             print('Ошибка. В списке не целые числа')
#             return False
#     return True  # No errors


def modify_list(lst: list, *funcs: callable) -> None:
    # print('\nВведены данные: ', lst)
    # if not is_validate_data(lst):
    #     print('На входе неверные значения')