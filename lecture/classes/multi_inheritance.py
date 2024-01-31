"""
В Python один класс может наследоваться сразу от нескольких родительских классов. Это называется множественным
наследованием. Дочерний класс может наследовать не только родительский класс, но и другой дочерний класс.
Такая форма наследования известна как многоуровневое наследование. Если два родительских класса имеют одинаковое имя
метода и дочерний класс (который наследует 2 родительских класса) вызывает этот метод, Python использует MRO
(порядок вызова методов) для вызова нужного метода
"""


class SuperClass1:
    ...
# Данные класса SuperClass1


class SuperClass2:
    ...
# Данные класса SuperClass2


class MultiDerived(SuperClass1, SuperClass2):
    ...
# Данные классов SuperClass1 + SuperClass2 + MultiDerived


class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth")


class WingedAnimal:
    def winged_animal(self):
        print("Winged animal can fly")


#  класс Bat является дочерним от двух родительских классов: Mammal и WingedAnimal
class Bat(Mammal, WingedAnimal):
    pass

b = Bat()
b.mammal_info()
b.winged_animal()


#  Многоуровневое наследование в Python

class SuperClass:
    ...
# Код родительского класса


class DerivedClass1(SuperClass):
    ...
# Код дочернего класса 1


class DerivedClass2(DerivedClass1):
    ...
# Код дочернего класса 2


class SuperClass:
    def super_method(self):
        print("Super class method")


class DerivedClass1(SuperClass):
    def derived1_method(self):
        print("Derived Class 1 method")


# Код дочернего класса 1
class DerivedClass2(DerivedClass1):

    def derived2_method(self):
        print("Derived Class 2 method")

#  Здесь DerivedClass2 является дочерним от класса DerivedClass1, который является дочерним от класса SuperClass.
#  Это означает, что DerivedClass2 наследует все атрибуты и методы как DerivedClass1, так и SuperClass.

d2 = DerivedClass2()

d2.super_method()
d2.derived2_method()
d2.derived1_method()
