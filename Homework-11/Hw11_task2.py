"""Задание 2:
Создайте класс Immutable, который представляет неизменяемый объект одного из типов str,
int, list, dict. Класс должен иметь атрибут value, который принимает значение при создании
объекта, и метод get_value, который возвращает значение атрибута. Класс должен запрещать
изменение атрибута value после создания объекта, а также создание новых атрибутов для
объекта. Для этого нужно переопределить методы setattr и delattr. Класс не должен иметь
инициализатор, установка значения должна осуществляться в методе new."""


class Immutable(int):

    def __new__(cls, value):
        cls.__value = value
        return int.__new__(cls, abs(value))
    def get_value(self) -> int:
        return self.__value

    def __setattr__(self, key, value):
        ...

    def __delattr__(self, item):
        ...


a = Immutable(65)
b = Immutable(-75)
# print(a.get_value())
print(b.get_value())
print(b, a)
print(id(a), id(b))


