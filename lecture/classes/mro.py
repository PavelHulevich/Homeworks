"""
Порядок вызова методов Method Resolution Order

Если два родительских класса имеют одинаковое имя метода и дочерний класс (который наследует 2 родительских класса)
вызывает этот метод, Python использует MRO (порядок вызова методов) для вызова нужного метода.
"""


class SuperClass1:

    def info(self):
        print("SuperClass1 info method")


class SuperClass2:

    def info(self):
        print("SuperClass2 info method")


# В данном случае MRO определяет, что методы должны наследоваться сначала от самого левого родительского класса
class Derived1(SuperClass1, SuperClass2):
    pass


d1 = Derived1()
"""
Здесь оба класса SuperClass1 и SuperClass2 имеют метод info(). Когда метод info() вызывается с помощью объекта d1 
класса Derived, Python использует MRO, чтобы определить, метод какого класса следует вызвать.
"""
d1.info()


class Derived2(SuperClass2, SuperClass1):
    pass


d2 = Derived2()
d2.info()


class MyMixin:

    def m1(self):
        print("MyMixin m1 method")

    def m2(self):
        print("MyMixin m2 method")


class SuperClass2:

    def info(self):
        print("SuperClass2 info method")


class Derived3(SuperClass2, MyMixin):
    pass


d3 = Derived3()
d3.info()
d3.m1()
d3.m2()


class Music: pass
class Rock(Music): pass
class Gothic(Music): pass
class Metal(Rock): pass
class GothicRock(Rock, Gothic): pass
class GothicMetal(Metal, Gothic): pass
class The69Eyes(GothicRock, GothicMetal): pass

"""
Иерархия наследований классов, объявленных выше

       Music
      /      \
   Rock      Gothic ------
   /     \        /       \
Metal    Gothic Rock       \
  |             |           \
   \------------------ Gothic Metal
                |          /
                The 69 Eyes

"""

#  Свойство __mro__ класса позволяет вывести порядок наследования методов из всех родительских классов

print(The69Eyes.__mro__)
