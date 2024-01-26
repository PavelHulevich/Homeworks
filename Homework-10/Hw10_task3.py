"""Задание 3:
Напишите декоратор, который будет декорировать функции, возвращающие как вложенные
так и плоские словари и добавлять к этим словарям ключи и значения в верхнем регистре,
сохраняя при этом структуру словаря. Для обхода вложенных словарей нужно использовать
рекурсию.

@upper_case
def f1() -> Dict[str, int]:
 return {'a': 1, 'b': 2}
f1() # {'a': 1, 'b': 2, 'A': 1, 'B': 2}

@upper_case
def f2() -> Dict[str, Union[str, int]]:
 return {'a': 'a', 'b': 'b'}
f2() # {'a': 'a', 'b': 'b', 'A': 'A', 'B': 'B'}

@upper_case
def f3() -> Dict[str, Union[str, int, List[Dict[str, int]]]]:
 return {'a': 'a', 'c': [{'b': 'b'}]}
f3() # {'a': 'a', 'A': 'A', 'C': [{'b': 'b', 'B': 'B'}], 'c': [{'b': 'b', 'B': 'B'}]}

@upper_case
def f4() -> Dict[str, Union[str, int, List[Dict[str, int]]]]:
 return {'a': 'a', 'c': [{'b': 1}, {'d': 2}]}
f4() # {'a': 'a', 'A': 'A', 'c': [{'b': 1}, {'d': 2}, {'B': 1}, {'D': 2}], 'C': [{'b': 1}, {'d': 2}, {'B': 1}, {'D':
2}]}"""
from typing import List, Dict, Union


def upper_case(func: callable) -> callable(Dict[str, Union[str, int]]):
    def upper_fn() -> callable(Dict[str, Union[str, int]]):
        def dict_to_upper(dict_in):
            for k, v in dict_in.items():
                dict_in = dict_in | {k.upper(): v}
                if isinstance(v, str):
                    dict_in = dict_in | {k.upper(): v.upper()}
            for k, v in dict_in.items():
                if isinstance(v, list):
                    list_temp = []
                    for index in v:
                        for k1, v1 in dict_to_upper(index).items():
                            list_temp.append({k1: v1})
                    dict_in[k] = list_temp
            return dict_in
        dict_fn = func()
        dict_fn = dict_to_upper(dict_fn)
        return dict_fn
    return upper_fn()


@upper_case
def f1() -> Dict[str, int]:
    return {'a': 1, 'b': 2}


@upper_case
def f2() -> Dict[str, Union[str, int]]:
    return {'a': 'a', 'b': 'b'}


@upper_case
def f3() -> Dict[str, Union[str, int, List[Dict[str, int]]]]:
    return {'a': 'a', 'c': [{'b': 'b'}]}


@upper_case
def f4() -> Dict[str, Union[str, int, List[Dict[str, int]]]]:
    return {'a': 'a', 'c': [{'b': 1}, {'d': 2}]}


print(f1)  # {'a': 1, 'b': 2, 'A': 1, 'B': 2}
print(f2)  # {'a': 'a', 'b': 'b', 'A': 'A', 'B': 'B'}
print(f3)  # {'a': 'a', 'A': 'A', 'C': [{'b': 'b', 'B': 'B'}], 'c': [{'b': 'b', 'B': 'B'}]}
print(f4)  # {'a': 'a', 'A': 'A', 'c': [{'b': 1}, {'d': 2}, {'B': 1}, {'D': 2}], 'C': [{'b': 1}, {'d': 2}, {'B': 1}, {'D':2}]}"""

