"""Задание 2:
Напишите второй декоратор для функции считающей факториал, но замеряющий время
работы этой функции для каждого списка чисел и выводящего время работы функции и
последовательность.
@slicer
@benchmark
def func2(seq: List[int]) -> List[int]:
 if len(seq) > 10:
 raise ...
 ...

 return new_seq

def func1() -> int:
 ...
"""
import time

class Error(Exception):
    ...

class ListTooLongError(Error):
    ...


def slicer(func: callable):
    # Декоратор
    def cut_list(list_in: list[int]) -> list[int]:
        # Нарезает списки на <= 10 элементов и скармливает func, которая в данном случае - func2.
        list_out = []
        while len(list_in) > 10:
            list_tmp = list_in[:10]
            del list_in[0:10]
            list_out.extend(func(list_tmp))
        list_out.extend(func(list_in))
        return list_out
    return cut_list


def benchmark(func) -> list:
    def time_exec(list_in: list):
        start = time.time()
        list_out = func(list_in)
        for i in range(0, 1000):
            a = i * i
        stop = time.time()
        timer = stop - start
        print(timer)
        return list_out
    return time_exec

@slicer
@benchmark
def func2(seq: list[int]) -> list[int]:
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


def func1(lst: list[int]) -> int:
    return sum(func2(lst))


def is_validate_data(list_in: list[int]) -> bool:
    # Проверка валидности исходных данных. На выходе False - если ошибка входных данных.
    if not isinstance(list_in, list):
        print('Ошибка. На входе не список')
        return False
    for number in list_in:
        if not isinstance(number, int):
            print('Ошибка. В списке не целые числа')
            return False
    return True  # No errors


def calculate_list_entry(list_in: list[int]) -> None:
    print('\nВведены значения: ', list_in)
    if is_validate_data(list_in):
        print('Результат расчета списка: ', func1(list_in))
    else:
        print('Введены неверные данные')


TEST_LIST = [[888, 3, 123, 2, 333, 4, 777, 3, 888, 2, 3, 4, 994, 888, 888,], [1, 2, 3], [2, 3, 4, 5, 6],
             6, 25, 'say', [2, 3, 'day', 5, 6], False, [1, [2, 6], 3], {45, 6}, 25.4]
for index in TEST_LIST:
    calculate_list_entry(index)
