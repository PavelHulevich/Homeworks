"""Задание 3:
Предположим, у нас есть класс Bird, который хранит информацию о птице и имеет метод
fly(), который позволяет птице летать. Класс выглядит примерно так:
class Bird:
 def __init__(self, name, wingspan):
 self.name = name
 self.wingspan = wingspan
 def fly(self):
 print(f"{self.name} is flying with wingspan {self.wingspan}")
Этот класс нарушает принцип LSP, потому что если мы создадим подкласс Penguin, который
наследуется от класса Bird, то мы не сможем использовать метод fly(), так как пингвины не
умеют летать. Если мы попытаемся вызвать метод fly() для объекта типа Penguin, то мы
получим нелогичный или ошибочный результат. Например:
class Penguin(Bird):
 def __init__(self, name, wingspan):
 super().__init__(name, wingspan)
p = Penguin("Pingu", 0.5)
p.fly() # Pingu is flying with wingspan 0.5
Чтобы исправить эту проблему необходимо сделать следующее:
• Создать абстрактный класс Animal, который будет содержать общие поля и методы для
всех животных, но не будет иметь метод fly().
• Создать подкласс FlyingAnimal, который будет наследоваться от класса Animal и добавлять
метод fly(), который будет реализовывать логику полета.
• Создать подклассы Bird и Bat, которые будут наследоваться от класса FlyingAnimal и
переопределять метод fly() в соответствии с их особенностями.
• Создать подкласс Penguin, который будет наследоваться от класса Animal, но не будет
иметь метод fly().
"""
from abc import ABC


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')


class FlyingAnimal(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} is flying with wingspan {self.wingspan}")

    def eat(self):
        print(f'{self.name} is eating feed')


class Bird(FlyingAnimal):
    def __init__(self, name, wingspan):
        super().__init__(name, wingspan)

    def fly(self):
        print(f"{self.name} - bird, is fast flying in the day with wingspan {self.wingspan}")

    def eat(self):
        print(f'{self.name} is eating grain')


class Bat(FlyingAnimal):
    def __init__(self, name, wingspan):
        super().__init__(name, wingspan)

    def fly(self):
        print(f"{self.name} - bat, is slow flying in the night with wingspan {self.wingspan}")

    def eat(self):
        print(f'{self.name} is eating insect')


class Penguin(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print(f'{self.name} is eating fish')


bee = FlyingAnimal('Bee', 1.5)
bee.fly()
bat = Bat('bat', 20)
bat.fly()

peng = Penguin('Peng')
peng.eat()
