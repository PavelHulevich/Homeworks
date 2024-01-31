"""
Наследование позволяет создать новый класс на основе существующего класса. Создаваемый новый класс называется
подклассом (дочерний или производный класс), а существующий класс, от которого получен дочерний класс, называется
суперклассом (родительский или базовый класс).

Польза от наследования в Python:
   Поскольку дочерний класс может наследовать функционал родительского класса, это позволяет повторно использовать код
   без его дублирования.
   Однажды разработав функционал, мы можем просто его наследовать. Нет необходимости изобретать велосипед по новой.
   Это делает код чище и проще в поддержке.
   Поскольку в дочерний класс можно добавлять собственный функционал, можно наследовать только нужный функционал
   родительского класса, а все остальное дописать в конкретном (дочернем) классе.
"""


# Определяем суперкласс
class SuperClass:
    ...
    # Атрибуты и методы суперкласса


# Наследование
class SubClass(SuperClass):
    ...
    # Атрибуты и метод super_class
    # Атрибуты и метод sub_class


class Vehicle:

    def __init__(self, wheels_number: int):
        self.wheels_number = wheels_number

    def move(self):
        pass


class Car(Vehicle):
    def __init__(self, wheels_number: int):
        super().__init__(wheels_number)
        self.wheels_number = wheels_number

    def move(self):
        print(f'car moved {self.wheels_number} wheels')


c = Car(4)
c.move()


class Animal:

    name = ''
    def eat(self):
        print('I eat')


class Dog(Animal):

    def display(self):
        print(f'My name is {self.name}')


labrador = Dog()

labrador.name = 'NAME'
labrador.eat()
labrador.display()


class Polygon:

    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def input_sides(self):
        self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.n)]

    def disp_sides(self):
        for i in range(self.n):
            print("Side", i + 1, "is", self.sides[i])


#  мы можем создать класс Triangle, который наследуется от класса Polygon. Это сделает все атрибуты класса Polygon
#  доступными для класса Triangle. Нам не нужно определять атрибуты и методы снова.
class Triangle(Polygon):

    def __init__(self):
        super().__init__(3)

    def find_area(self):
        a, b, c = self.sides

        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

        print('The area of the triangle is %0.2f' % area)


t = Triangle()
t.input_sides()
t.find_area()


#  Переопределение методов в наследовании


class Animal:
    # Атрибуты и метод суперкласса
    name = ""
    def eat(self):
        print("I can eat")


# Наследуем от класса Animal
class Dog(Animal):
    # Переопределяем метод eat()
    def eat(self):
        print("I like to eat bones")


# Создаем объект подкласса
labrador = Dog()
# Вызываем метод eat() через объект класса Dog
labrador.eat()


#  Метод super() в наследовании

class Animal:

    name = ''
    def eat(self):
        print('I eat')


class Dog(Animal):

    def eat(self):
        super().eat()  # Вызываем метод eat() родительского класса с помощью дополнительного метода super()
        print('I eat bones')

    def display(self):
        print(f'My name is {self.name}')

d = Dog()
d.eat()
