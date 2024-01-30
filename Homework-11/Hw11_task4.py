"""Задание 4:
Создайте 2 класса для работы с килограммами и фунтами. Каждый класс должен содержать
метод для перевода одних единиц в другие. Каждый класс должен содержать метод для
увеличения значения. Каждый класс должен уметь складывать и вычитать разные единицы,
т.е. килограммы с килограммами, килограммы с фунтами, фунты с фунтами. Классы не
поддерживают отрицательные значения, при значении < 0 класс должен выбрасывать ошибку.
Класс для работы с килограммами не поддерживает значение >= 1000 кг, он возвращает
исключение. Класс для работы с фунтами не поддерживает значение >= 14 фунтов, он
возвращает исключение. Информационная строка об объекте класса __repr__ должна
возвращать значение, единицы измерения килограмм или фунт, значение в граммах или
унциях."""
from typing import Optional, Union, Self, TypeVar


class Kilograms:
    MIN_KG, MAX_KG = 0, 1000

    def __init__(self, value: float):
        if self.MIN_KG <= value < self.MAX_KG:
            self.value = value
        elif value >= self.MAX_KG:
            print(f'Ошибка. Значение больше либо равно {self.MAX_KG} кг.')
        else:
            print(f'Ошибка. Значение меньше  {self.MIN_KG} кг.')

    def __repr__(self) -> str:
        return f'Вес в килограммах: {self.value} кг.  Вес в граммах:  {self.value * 1000} г.'

    def get_value(self) -> float:
        return self.value

    def to_pound(self) -> float:
        # Перевод в фунты-1
        return self.value * 2.2

    def __call__(self) -> float:
        # Перевод в фунты-2
        return self.value * 2.2

    def __add__(self, other) -> Optional[float]:
        if type(other).__name__ == 'Pounds':
            value_out = self.value + other.get_value() * 0.45
        elif type(other).__name__ == 'Kilograms':
            value_out = self.value + other.get_value()
        else:
            value_out = self.value + other
        if value_out >= self.MAX_KG:
            print(f'Ошибка. Вес больше либо равен {self.MAX_KG} кг.')
        else:
            return value_out

    def __sub__(self, other) -> Optional[float]:
        if type(other).__name__ == 'Pounds':
            value_out = self.value - other.get_value() * 0.45
        elif type(other).__name__ == 'Kilograms':
            value_out = self.value - other.get_value()
        else:
            value_out = self.value - other
        if value_out < self.MIN_KG:
            print(f'Ошибка. Вес меньше {self.MIN_KG} кг.')
        else:
            return value_out


class Pounds:
    MIN_LB, MAX_LB = 0, 14

    def __init__(self, value: float):
        if self.MIN_LB <= value < self.MAX_LB:
            self.value = value
        elif value >= self.MAX_LB:
            print(f'Ошибка. Значение больше либо равно {self.MAX_LB} Lb')
        else:
            print(f'Ошибка. Значение меньше  {self.MIN_LB} Lb')

    def __repr__(self: Self) -> str:
        return f'Вес в фунтах: {self.value} Lb.  Вес в унциях:  {self.value * 12} oz.'

    def get_value(self: Self) -> float:
        return self.value

    def to_kilogram(self: Self) -> float:
        return self.value * 0.45

    def __call__(self: Self) -> float:
        return self.value * 0.45

    def __add__(self, other: Union[Self, Kilograms]) -> Optional[float]:
        if type(other).__name__ == 'Kilograms':
            value_out = self.value + other.get_value() * 2.2
        elif type(other).__name__ == 'Pounds':
            value_out = self.value + other.get_value()
        else:
            value_out = self.value + other
        if value_out >= self.MAX_LB:
            print(f'Ошибка. Вес больше либо равен {self.MAX_LB} Lb.')
        else:
            return value_out

    def __sub__(self, other: Union[Self, Kilograms]) -> Optional[float]:
        if type(other).__name__ == 'Kilograms':
            value_out = self.value - other.get_value() * 2.2
        elif type(other).__name__ == 'Pounds':
            value_out = self.value - other.get_value()
        else:
            value_out = self.value - other
        if value_out < self.MIN_LB:
            print(f'Ошибка. Вес меньше {self.MIN_LB} Lb.')
        else:
            return value_out



print('\n==============ТЕСТИРОВАНИЕ КЛАССА Kilograms==============')
TEST_TUPLE_KG = ('weight_kg_1 = Kilograms(5)', 'weight_kg_2 = Kilograms(1)',
                 'weight_lb_1 = Pounds(10)', 'weight_lb_2 = Pounds(3)',
                 'print(weight_kg_1())', 'print(weight_kg_1.to_pound())',
                 'print(weight_kg_1 + weight_kg_1)', 'print(weight_kg_1 + weight_kg_2)',
                 'print(weight_kg_1 + weight_lb_1)', 'print(weight_kg_1 + 20)',
                 'print(weight_kg_1 - weight_kg_1)', 'print(weight_kg_1 - weight_kg_2)',
                 'print(weight_kg_1 - weight_lb_1)', 'print(weight_kg_1 - 4)',
                 'print(weight_kg_1 - 10)', 'print(weight_kg_1 + 1000)',
                 'print(weight_kg_1.__repr__())')
for tupleCur in TEST_TUPLE_KG:
    print(f'\nВыполняем команду: {tupleCur}')
    exec(tupleCur)

print('\n===============ТЕСТИРОВАНИЕ КЛАССА Pounds===============')
TEST_TUPLE_LB = ('print(weight_lb_1 + weight_lb_2)', 'print(weight_lb_1 - weight_lb_2)',
                 'print(weight_lb_1 + weight_kg_2)', 'print(weight_lb_1 - weight_kg_2)',
                 'print(weight_lb_1 + weight_kg_1)', 'print(weight_lb_1 - 15)',
                 'print(weight_lb_2.__repr__())')
for tupleCur in TEST_TUPLE_LB:
    print(f'\nВыполняем команду: {tupleCur}')
    exec(tupleCur)


