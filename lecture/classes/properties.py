"""
Свойством называется такой метод класса, работа с которым подобна работе с атрибутом.
Для объявления метода свойством необходимо использовать декоратор @property.

Важным преимуществом работы через свойства является то, что вы можете осуществлять проверку входных значений,
перед тем как присвоить их атрибутам.
"""


class Rectangle:

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if w > 0:
            self.__width = w
        else:
            raise ValueError

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if h > 0:
            self.__height = h
        else:
            raise ValueError

    def area(self):
        return self.__width * self.__height


#  работать с width и height можно так, как будто они являются атрибутами
rect = Rectangle(10, 20)
print(rect.width)
print(rect.height)


#  можно не только читать, но и задавать новые значения свойствам

rect.width = 50
print(rect.width)

rect.height = 70
print(rect.height)

try:
    rect.width = -10
except ValueError:
    pass
