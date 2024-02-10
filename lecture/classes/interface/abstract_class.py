"""
В теории объектно-ориентированного программирования есть понятия интерфейсов и абстрактных классов. Эти классы созданы
для того, чтобы быть отнаследованными в других классах. Интерфейс и абстрактный класс созданы для того, чтобы показать,
какими свойствами и методами должны обладать все их дочерние классы. Разница интерфейса и абстрактного класса в том, что
интерфейс не содержит реализации, а абстрактный класс может помимо абстрактных методов содержать и часть реализованных
методов.

Абстрактный класс — это класс, который не может быть инстанциирован, то есть нельзя создать его экземпляр. Он
представляет собой шаблон или чертеж для создания других классов. Абстрактный класс может содержать абстрактные методы
(методы без реализации) и/или обычные методы
"""
from abc import ABC, abstractmethod


class AbstractClassExample(ABC):

    @abstractmethod
    def do_something(self):
        pass


try:
    m = AbstractClassExample()
    m.do_something()
except TypeError:
    pass


class Myclass(AbstractClassExample):
    pass


try:
    m = Myclass()
    m.do_something()
except TypeError:
    pass


class Myclass2(AbstractClassExample):

    def do_something(self):
        pass


m = Myclass2()
m.do_something()


"""
В Python нет встроенной поддержки интерфейсов. Однако концепцию интерфейса можно реализовать с помощью абстрактного 
класса, в котором все методы являются абстрактными.
"""


class InterfaceExample(ABC):

    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass

"""
В этом примере InterfaceExample — это интерфейс, который содержит два абстрактных метода: method1 и method2. Любой 
класс, который наследует InterfaceExample, должен реализовать оба этих метода.
"""