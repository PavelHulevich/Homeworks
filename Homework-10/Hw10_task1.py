"""Задание 1:
Напишите функцию, которая принимает список чисел произвольной длинны, передает этот
список во вторую функцию для дальнейших вычислений, суммирует результат вычислений и
возвращает сумму всех элементов последовательности.
Вторая функция считает факториал каждого числа из последовательности и возвращает
список факториалов этих чисел. Для вычисления факториала надо реализовать вложенную
функцию внутри второй функции. Вложенная функция должно вычислять факториал
рекурсивно.
Вторая функция не может обрабатывать список, содержащий больше 10 чисел за один вызов
функции. Если в списке больше 10 элементов функция должна выбросить кастомное
исключение с текстом ошибки о превышении максимального количества элементов.
Чтобы ограничить длинну последовательности необходимо реализовать декоратор, который
будет принимать исходную последовательность, нарезать ее на списки состоящие из не более
чем 10 элементов и передавать эти списки декорируемой функции. Декоратор должен
накапливать результат работы декорируемой функции и возвращать вызывающей функции
список, включающий в себя все элементы.
@slicer
def func2(seq: List[int]) -> List[int]:
if len(seq) > 10:
raise ...
...

return new_seq

def func1() -> int:
 ...
"""
from typing import List, Callable


class Error(Exception):
    ...


class ListTooLongError(Error):
    ...


def slicer(func: Callable[[List[int]], List[int]]) -> Callable[[List[int]], List[int]]:
    # Декоратор
    def cut_list(list_in: List[int]) -> List[int]:
        # Нарезает списки на <= 10 элементов и скармливает func, которая в данном случае - func2.
        list_out = []
        while len(list_in) > 10:
            list_tmp = list_in[:10]
            del list_in[0:10]
            list_out.extend(func(list_tmp))
        list_out.extend(func(list_in))
        return list_out
    return cut_list


@slicer
def func2(seq: List[int]) -> List[int]:
    # Расчет факториала для каждого элемента списка.
    def factorial(num: int) -> int:
        # Расчет факториала рекурсией.
        if num == 1:
            return num
        return num * factorial(num - 1)

    try:
        if len(seq) > 10:
            raise ListTooLongError
        else:
            new_seq = []
            for number in seq:
                new_seq.append(factorial(number))
            return new_seq   # Возвращает новый список с элементами, равными факториалам элементов входного списка.
    except ListTooLongError:  # Отработка ошибки кастомным классом
        print('Список слишком длинный')
        exit(100)


def func1(lst: List[int]) -> int:
    return sum(func2(lst))


def is_validate_data(list_in: List[int]) -> bool:
    # Проверка валидности исходных данных. На выходе False - если ошибка входных данных.
    if not isinstance(list_in, list):
        print('Ошибка. На входе не список')
        return False
    for number in list_in:
        if not isinstance(number, int):
            print('Ошибка. В списке не целые числа')
            return False
    return True  # No errors


def calculate_list_entry(list_in: List[int]) -> None:
    print('\nВведены значения: ', list_in)
    if is_validate_data(list_in):
        print('Результат расчета списка: ', func1(list_in))
    else:
        print('Введены неверные данные')


TEST_LIST = [[2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4,], [1, 2, 3], [2, 3, 4, 5, 6],
             6, 25, 'say', [2, 3, 'day', 5, 6], False, [1, [2, 6], 3], {45, 6}, 25.4]
for index in TEST_LIST:
    calculate_list_entry(index)
