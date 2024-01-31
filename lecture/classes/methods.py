"""
В Python существует три различных типа методов: статический метод, метод класса и метод экземпляра.
Каждый из них имеет разные характеристики и должен использоваться в разных ситуациях.

Статический метод в Python необходимо создать, добавив @staticmethod. Это позволяет Python знать, что метод должен быть
статическим. Основной характеристикой статического метода является то, что его можно вызывать без создания экземпляра
класса. Эти методы являются автономными, что означает, что они не могут получить доступ к какому-либо другому атрибуту
или вызвать какой-либо другой метод внутри этого класса
"""


class Math:
    @staticmethod
    def factorial(number):
        if number == 0:
            return 1
        else:
            return number * Math.factorial(number - 1)


factorial = Math.factorial(5)
print(factorial)

print(Math.factorial(3))


"""
Методы класса должны создаваться с помощью @classmethod, метод можно вызывать, не имея экземпляра класса. 
Разница заключается в возможности доступа к другим методам и атрибутам класса, но не к атрибутам экземпляра.

classmethod должен создавать объект этого же типа.
"""


class Math:

    def __init__(self, multiplier: int):
        self.multiplier = multiplier

    @staticmethod
    def factorial(number):
        if number == 0:
            return 1
        else:
            return number * Math.factorial(number - 1)

    @classmethod
    def mul_10(cls):
        return cls(10)

    def multiply(self, x: int):
        return x * self.multiplier


print(Math.factorial(5))
m = Math.mul_10()
print(m.multiply(10))
print(Math.mul_10().multiply(20))


"""
метод экземпляра может быть вызван только в том случае, если класс был создан. Как только объект этого класса создан, 
может быть вызван метод экземпляра, который может получить доступ ко всем атрибутам этого класса через 
зарезервированное слово self.

"""

b = Math(20)
print(b.multiply(20))
