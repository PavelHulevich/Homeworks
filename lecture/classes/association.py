"""
Ассоциация – это когда один класс включает в себя другой класс в качестве одного из полей.
Ассоциация описывается словом «имеет». Автомобиль имеет двигатель. Вполне естественно, что он не будет являться
наследником двигателя (хотя такая архитектура тоже возможна в некоторых ситуациях).
"""


#  Композиция – это когда двигатель не существует отдельно от автомобиля. Он создается при создании автомобиля и
#  полностью управляется автомобилем. В типичном примере, экземпляр двигателя будет создаваться в конструкторе
#  автомобиля.
class Engine:

    def __init__(self, hp):
        self.hp = hp


class Car:

    def __init__(self, wn):
        self.wn = wn

    def move(self):
        engine = Engine(500)
        print(f'car moved {self.wn} wheels. {engine.hp} horse powers')


c = Car(4)
c.move()

#  инициализация класса Engine параметрами через класс Car


class Engine:

    def __init__(self, hp):
        self.hp = hp


class Car:

    def __init__(self, wn, hp):
        self.wn = wn
        self.hp = hp

    def move(self):
        engine = Engine(self.hp)
        print(f'car moved {self.wn} wheels. {engine.hp} horse powers')


c = Car(4, 400)
c.move()


#  Агрегация – это когда экземпляр двигателя создается где-то в другом месте кода, и передается в конструктор
#  автомобиля в качестве параметра.
class Car2:

    def __init__(self, wn: int, engine: Engine):
        self.wn = wn
        self.engine = engine

    def move(self):
        print(f'car moved {self.wn} wheels. {self.engine.hp} horse powers')


e = Engine(500)
c2 = Car2(4, e)
c2.move()


