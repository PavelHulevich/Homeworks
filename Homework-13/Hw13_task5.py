"""Задание 5:
Предположим, у нас есть класс Order, который хранит информацию о заказе и имеет метод
process(), который обрабатывает заказ и сохраняет его в базу данных. Класс выглядит
примерно так:
class Order:
 def __init__(self, items, total):
 self.items = items
 self.total = total
 def process(self):
 db = Database() # создаем объект класса Database
 db.connect() # подключаемся к базе данных
 db.save(self) # сохраняем заказ в базе данных
Этот класс нарушает принцип DIP, потому что он зависит от конкретного класса Database,
который реализует работу с базой данных. Если мы захотим изменить способ хранения
заказов, например, использовать файлы или облачные сервисы, то нам придется изменить код
класса Order. Это может привести к ошибкам, сложности тестирования и нарушению работы
существующего кода, который использует этот класс.
Чтобы исправить эту проблему, необходимо сделать следующее:
• Создать интерфейс Storage, который будет содержать метод save(), который принимает
объект заказа и сохраняет его в каком-то хранилище.
• Создать класс Database, который будет реализовывать интерфейс Storage и иметь методы
connect() и save(), которые будут работать с базой данных.
• Создать класс File, который будет реализовывать интерфейс Storage и иметь метод save(),
который будет сохранять заказ в файл.
• Изменить класс Order, чтобы он не создавал объект класса Database, а принимал объект
типа Storage в качестве параметра в методе process(). Таким образом, класс Order не будет
знать о деталях реализации хранилища, а будет использовать общий интерфейс."""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Storage(ABC):
    def __init__(self):
        ...

    @abstractmethod
    def save(self) -> None:
        ...


class Database(Storage):
    def __init__(self):
        super().__init__()

    @staticmethod
    def connect() -> None:
        print('Подключаемся к базе данных для сохранение')

    def save(self: Order) -> None:
        print(f'Сохраняем заказ {self} в базе данных')


class File(Storage):
    def __init__(self):
        super().__init__()

    def save(self: Order) -> None:
        print(f'Сохраняем заказ {self} в файл')


class Order:
    def __init__(self, items: List[str], total: float):
        self.items = items
        self.total = total

    def __str__(self):
        return f'Заказ: {self.items} на сумму: {self.total} '

    def process(self):
        Database.connect()
        Database.save(self)


a = Order(['wdwd', 'zazaz', 'rfrfrfr'], 125)
a.process()
