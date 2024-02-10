"""
Структурная типизация (structural type system) определяет совместимость типов на основе структуры этих типов, а не на
явных декларациях. Подобный механизм может рассматриваться как некоторый аналог утиной типизации, но для статических
проверок.
в Python 3.8 появились протоколы. Протоколы определяют «интерфейсы», описывающие ожидаемые атрибуты и методы, и, при
необходимости, организуют проверку наличия всего этого в соответствующих классах
"""
from typing import Protocol


class Animal(Protocol):
    def feed(self) -> None:
        pass


class Duck:
    def feed(self) -> None:
        print("Duck eats")


def feed(animal: Animal) -> None:
    animal.feed()


duck = Duck()
feed(duck)


"""
Как видно, Animal — это теперь протокол (Protocol). Класс Duck не является наследником какого-либо базового класса. 
Но mypy всё это полностью устраивает.
Протоколы поддерживают создание подклассов, то есть — определение дочерних протоколов, являющихся наследниками 
родительских протоколов и расширяющих их возможности. При создании подклассов протоколов главное помнить о том, что 
наследственные отношения надо устанавливать и с родительским протоколом, и с typing.Protocol
"""


from typing import Protocol


class Animal(Protocol):
    def feed(self) -> None:
        pass


class Bird(Animal, Protocol):
    def fly(self) -> None:
        pass


class Duck:
    def feed(self) -> None:
        print("Duck eats")

    def fly(self) -> None:
        print("Duck flies")


def feed(animal: Animal) -> None:
    animal.feed()


def feed_bird(bird: Bird) -> None:
    bird.feed()
    bird.fly()


duck = Duck()
feed_bird(duck)
