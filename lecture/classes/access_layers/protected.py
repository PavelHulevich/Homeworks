"""
Существуют 3 типа доступа к атрибутам:
    • Публичные Public. Можем обращаться и менять вне класса.

    • Приватные Private (_одно подчеркивание перед названием атрибута). Также можем обращаться и менять вне класса,
      но подчеркивание говорит другим разработчикам, что туда лучше напрямую не лезть.

    • Защищенные Protected (__ два подчеркивания перед названием атрибута). Обращаться напрямую к защищенным атрибутам
      мы не можем. Только через отдельные созданные для этого методы. Т.е. мы создаем незащищенный метод и в нем уже
      обращаемся к защищенным атрибутам и возвращаем через return. А дальше при создании экземпляра класса можем
      обращаться к этим методам, как к любым другим.
"""

#  Если атрибут или метод начинается с двух подчеркиваний, то тут напрямую вы к нему уже не обратитесь


class Rectangle:

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, w):
        self.__width = w

    def get_height(self):
        return self.__height

    def set_height(self, h):
        self.__height = h

    def area(self):
        return self.__width * self.__height

#  Попытка обратиться к __width напрямую вызовет ошибку, нужно работать только через get_width():

rect = Rectangle(10, 20)
print(rect.get_width())

try:
    rect.__width
except AttributeError:
    pass


#  Обратиться к атрибуту и изменить его можно, но название атрибута теперь такое _Rectangle__width
print(rect._Rectangle__width)
rect._Rectangle__width = 20
print(rect.get_width())
