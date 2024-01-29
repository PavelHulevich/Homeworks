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


class Kilograms:
    MIN_KG, MAX_KG = 0, 1000

    def __init__(self, kilogram: float = 0):
        self.kilogram = kilogram

    def __repr__(self) -> str:
        return f'Вес в килограммах: {self.kilogram} кг.  Вес в граммах:  {self.kilogram * 1000} г.'

    def is_validate(self, value: float) -> bool:
        # Валидация входных данных.
        is_not_error = True  # Флаг отсутствия ошибки входных данных. По умолчанию "Истина" - ошибок нет.
        if not isinstance(value, (int, float)):
            print('Ошибка. На входе не число')
            is_not_error = False
        return is_not_error

    def kilogram_to_pound(self) -> float:
        return self.kilogram * 2.2

    def kilogram_increment(self) -> None:
        if self.kilogram + 1 < self.MAX_KG:
            self.kilogram += 1
        else:
            print(f'Ошибка. Вес больше {self.MAX_KG} кг.')

    def kilogram_add_kilogram(self, value: float) -> None:
        if self.is_validate(value):
            if (self.kilogram + value) < self.MAX_KG:
                self.kilogram += value
            else:
                print(f'Ошибка. Вес больше {self.MAX_KG} кг.')
        else:
            print('Неверные входные данные')

    def kilogram_add_pound(self, value: float) -> None:
        if self.is_validate(value):
            if self.kilogram + value * 0.45 < self.MAX_KG:
                self.kilogram += value * 0.45
            else:
                print(f'Ошибка. Вес больше {self.MAX_KG} кг.')
        else:
            print('Неверные входные данные')

    def kilogram_sub_kilogram(self, value: float) -> None:
        if self.is_validate(value):
            if self.kilogram - value >= self.MIN_KG:
                self.kilogram -= value
            else:
                print(f'Ошибка. Вес меньше {self.MIN_KG} кг.')
        else:
            print('Неверные входные данные')

    def kilogram_sub_pound(self, value: float) -> None:
        if self.is_validate(value):
            if self.kilogram - value * 0.45 >= self.MIN_KG:
                self.kilogram -= value * 0.45
            else:
                print(f'Ошибка. Вес меньше {self.MIN_KG} кг.')
        else:
            print('Неверные входные данные')


class Pounds:
    MIN_LB, MAX_LB = 0, 14

    def __init__(self, pound: float = 0):
        self.pound = pound

    def __repr__(self) -> str:
        return f'Вес в фунтах: {self.pound} Lb  Вес в унциях:  {self.pound * 16} oz'

    def is_validate(self, value: float) -> bool:
        # Валидация входных данных.
        is_not_error = True  # Флаг отсутствия ошибки входных данных. По умолчанию "Истина" - ошибок нет.
        if not isinstance(value, (int, float)):
            print('Ошибка. На входе не число')
            is_not_error = False
        return is_not_error

    def pound_to_kilogram(self) -> float:
        return self.pound * 0.45

    def pound_increment(self) -> None:
        if self.pound + 1 < self.MAX_LB:
            self.pound += 1
        else:
            print(f'Ошибка. Вес больше {self.MAX_LB} Lb.')

    def pound_add_pound(self, value: float) -> None:
        if self.is_validate(value):
            if self.pound + value < self.MAX_LB:
                self.pound += value
            else:
                print(f'Ошибка. Вес больше {self.MAX_LB} Lb.')
        else:
            print('Неверные входные данные')

    def pound_add_kilogram(self, value: float) -> None:
        if self.is_validate(value):
            if self.pound + value * 2.2 < self.MAX_LB:
                self.pound += value * 2.2
            else:
                print(F'Ошибка. Вес больше {self.MAX_LB} Lb.')
        else:
            print('Неверные входные данные')

    def pound_sub_pound(self, value: float) -> None:
        if self.is_validate(value):
            if self.pound - value >= self.MIN_LB:
                self.pound -= value
            else:
                print(f'Ошибка. Вес меньше {self.MIN_LB} Lb.')
        else:
            print('Неверные входные данные')

    def pound_sub_kilogram(self, value: float) -> None:
        if self.is_validate(value):
            if self.pound - value * 2.2 >= self.MIN_LB:
                self.pound -= value * 2.2
            else:
                print(f'Ошибка. Вес меньше {self.MIN_LB} Lb.')
        else:
            print('Неверные входные данные')


print('\n==============ТЕСТИРОВАНИЕ КЛАССА Kilograms==============')
TEST_TUPLE_KG = ('weightKG = Kilograms(5)', 'print(weightKG.__repr__())',
                 'print(weightKG.kilogram)', 'print(weightKG.kilogram_to_pound())',
                 'weightKG.kilogram_add_kilogram(1000)', 'print(weightKG.__repr__())',
                 'weightKG.kilogram_add_kilogram(10.5)', 'print(weightKG.__repr__())',
                 'weightKG.kilogram_add_kilogram("a")', 'print(weightKG.__repr__())',
                 'weightKG.kilogram_sub_kilogram(20)', 'print(weightKG.__repr__())',
                 'weightKG.kilogram_sub_pound(5)', 'print(weightKG.__repr__())')
for tupleCur in TEST_TUPLE_KG:
    print(f'\nВыполняем команду: {tupleCur}')
    exec(tupleCur)

print('\n===============ТЕСТИРОВАНИЕ КЛАССА Pounds===============')
TEST_TUPLE_LB = ('weightLB = Pounds(5)', 'print(weightLB.__repr__())',
                 'print(weightLB.pound)',
                 'print(weightLB.pound_to_kilogram())',
                 'weightLB.pound_add_kilogram(2)', 'print(weightLB.__repr__())',
                 'weightLB.pound_add_pound(11)', 'print(weightLB.__repr__())',
                 'weightLB.pound_add_pound("a")', 'print(weightLB.__repr__())',
                 'weightLB.pound_sub_kilogram(20)', 'print(weightLB.__repr__())',
                 'weightLB.pound_sub_kilogram(1)', 'print(weightLB.__repr__())')
for tupleCur in TEST_TUPLE_LB:
    print(f'\nВыполняем команду: {tupleCur}')
    exec(tupleCur)