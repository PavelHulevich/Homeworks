"""Задание 1:
Создайте класс Shape, который будет представлять абстрактную геометрическую фигуру.
Класс должен иметь метод area, который возвращает площадь фигуры, и метод perimeter,
который возвращает периметр фигуры. Затем создайте классы Circle, Rectangle и Triangle,
которые будут наследовать от класса Shape и переопределять методы area и perimeter
согласно формулам для соответствующих фигур. Также добавьте инициализаторы для
каждого класса, которые будут принимать параметры, необходимые для определения фигуры
(например, радиус для круга, длина и ширина для прямоугольника, три стороны для
треугольника).
"""
from abc import ABC, abstractmethod
from math import pi, sqrt


class Shape(ABC):
    @abstractmethod
    def area(self):
        ...

    @abstractmethod
    def perimetr(self):
        ...


class Circle(Shape):

    def __init__(self, radius: float):
        self.radius = radius

    def __str__(self) -> str:
        return f'Окружность с радиусом: {self.radius}.'

    def area(self) -> float:
        return pi * self.radius ** 2

    def perimetr(self) -> float:
        return pi * self.radius * 2


class Rectangle(Shape):
    def __init__(self, side_a: float, side_b: float):
        self.side_a = side_a
        self.side_b = side_b

    def __str__(self) -> str:
        return f'Прямоугольник со сторонами: {self.side_a} и {self.side_b}.'

    def area(self) -> float:
        return self.side_a * self.side_b

    def perimetr(self) -> float:
        return 2 * (self.side_a + self.side_b)


class Triangle(Shape):
    def __init__(self, side_a: float, side_b: float, side_c: float):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.half_perimetr = (self.side_a + self.side_b + self.side_c) / 2

    def __str__(self) -> str:
        return f'Треугольник со сторонами: {self.side_a}, {self.side_b}, {self.side_c}.'

    def area(self) -> float:
        return sqrt((self.half_perimetr - self.side_a) * (self.half_perimetr - self.side_b) *
                    (self.half_perimetr - self.side_c) * self.half_perimetr)

    def perimetr(self) -> float:
        return self.half_perimetr * 2
    

TEST_LIST = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9]

circle = Circle(3)
rectangle = Rectangle(3, 5)
triangle = Triangle(3, 4, 5)
print(f'{circle} Длина окружности {circle.perimetr():2.5}. Площадь круга: {circle.area():2.5}.')
print(f'{rectangle} Периметр: {rectangle.perimetr()}. Площадь: {rectangle.area()}.')
print(f'{triangle} Периметр: {triangle.perimetr()}. Площадь: {triangle.area()}.')
