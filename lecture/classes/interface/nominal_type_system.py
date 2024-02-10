"""
При номинальной типизации (nominal type system) совместимость типов определяется, основываясь на явных декларациях в
коде программы, например, на именах классов и иерархии наследования. Если класс Duck явно объявлен наследником класса
Bird, то объекты класса Duck могут быть использованы везде, где ожидаются объекты класса Bird. Применительно к Python,
mypy может статически, без непосредственного запуска программы, основываясь только на исходном коде, проверить такую
совместимость.
"""


class Bird:
    def feed(self) -> None:
        print("Feeding the bird...")


class Duck(Bird):
    def feed(self) -> None:
        print("Feeding the duck...")


class Goose:
    """
    Этот класс по каким-то причинам не объявлен наследником класса Bird.
    """
    def feed(self) -> None:
        print("Feeding the goose...")


def feed(bird: Bird) -> None:
    bird.feed()


# OK
feed(Bird())
# OK
feed(Duck())

# Mypy error: Argument 1 to "feed" has incompatible type "Goose";
#  expected "Bird"
feed(Goose())
# класс Goose имеет нужный нам метод feed, с точки зрения номинальной типизации он не является подтипом Bird, о чем
# сообщает mypy

try:
    # Mypy error: Argument 1 to "feed" has incompatible type "None";
    #  expected "Bird"
    feed(None)
except AttributeError:
    pass
