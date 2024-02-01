"""Задание 3:
Создайте класс Vehicle, который будет представлять транспортное средство. Класс должен
иметь атрибуты brand, model, color и метод start, который выводит сообщение "The vehicle is
starting". Затем создайте классы Car, Bike и Plane, которые будут наследовать от класса
Vehicle и добавлять свои специфические атрибуты и методы. Например, класс Car может
иметь атрибут doors, который указывает количество дверей, и метод honk, который выводит
сообщение "The car is honking". Класс Bike может иметь атрибут gears, который указывает
количество скоростей, и метод pedal, который выводит сообщение "The bike is pedaling".
Класс Plane может иметь атрибут wingspan, который указывает размах крыльев, и метод fly,
который выводит сообщение "The plane is flying"."""


class Vehicles:
    def __init__(self, brand: str, model: str, color: str):
        self.brand = brand
        self.model = model
        self.color = color

    def start(self) -> None:
        print('The vehicle is starting')


class Car(Vehicles):
    def __init__(self, brand: str, model: str, color: str, doors: int):
        super().__init__(brand, model, color)
        self.doors = doors

    def honk(self) -> None:
        print('The car is honking')


class Bike(Vehicles):
    def __init__(self, brand: str, model: str, color: str, gears: int):
        super().__init__(brand, model, color)
        self.gears = gears

    def pedal(self) -> None:
        print('The bike is pedaling')


class Plane(Vehicles):
    def __init__(self, brand: str, model: str, color: str, wingspan: int):
        super().__init__(brand, model, color)
        self.wingspan = wingspan

    def fly(self) -> None:
        print('The plane is flying')

