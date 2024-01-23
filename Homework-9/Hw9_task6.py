"""Задание 6:
Напишите функцию для разворота числа (представления числа в обратном порядке) с
помощью рекурсии. В решении можно пользоваться только типом int и никакими другими
типами данных."""


def reverse_number(integer_in: int, integer_out: int = 0) -> int:
    if not integer_in:
        return integer_out
    integer_out = integer_in % 10 + integer_out*10
    return reverse_number(integer_in // 10, integer_out)


def is_validate_data(number: int) -> bool:
    # Проверка валидности исходных данных. На выходе False - если ошибка входных данных.
    if not isinstance(number, int):
        print('Ошибка. На входе не целое число')
        return False
    return True  # No errors