"""
Классы используются для создания определяемых пользователем структур данных. Кроме того, классы определяют функции,
называемые методами, которые определяют поведение и действия, которые объект, созданный на основе класса, может
выполнять с его данными.
Класс — это схема того, как что-то должно быть определено. Говоря иначе, класс — это как форма или анкета.
Экземпляр — это как форма, заполненная информацией. Как многие люди могут заполнить одну и ту же анкету своей
собственной уникальной информацией, так и из одного класса можно создать множество разных экземпляров.
"""


class Dog:

    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age


dog = Dog(name='Rex', age=12)
print(dog.species)
print(dog.name)


class Rectangle:
    default_color = "green"  # статический атрибут

    def __init__(self, width, height):
        self.width = width  # динамический атрибут
        self.height = height  # динамический атрибут


print(Rectangle.default_color)

Rectangle.default_color = 'blue'
print(Rectangle.default_color)


class MyClass:

    def my_method(self):
        print("my_method")

    @staticmethod
    def static_method(self):
        print(self)
        pass

    @classmethod
    def class_method(cls):
        return MyClass()


print(MyClass.static_method('param'))

a = MyClass.class_method()
print(type(a))

my_class = MyClass()
my_class.my_method()
