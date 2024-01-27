"""Задание 1:
Создайте класс очереди задач, который будет реализовывать следующие методы:
• добавление элемента в очередь
• извлечение элемента из очереди
• проверка на пустоту
• очистка очереди
• получение размера очереди
Для хранения элементов используйте список. Очередь не может содержать больше 20
элементов, в случае добавления нового элемента в очередь, в которой уже есть 20 элементов,
метод должен вернуть исключение. В случае с извлечением элемента из пустой очереди
метод должен вернуть исключение."""
from typing import Optional


class Error(Exception):
    ...


class ListTooLongError(Error):
    ...


class ListEmptyError(Error):
    ...


class Queue:
    def __init__(self, max_queue):
        self.max_queue = max_queue
        self.queue_list = []

    def add(self, str_in):
        try:
            if self.len() >= self.max_queue:
                raise ListTooLongError
            self.queue_list.append(str_in)
            print(str_in, self.queue_list)
        except ListTooLongError:
            print(f'Задача не добавлена. Список задач достиг максимального размера в {self.max_queue} элементов.')

    def extract(self) -> Optional[str]:
        try:
            if not self.len():
                raise ListEmptyError
            return self.queue_list.pop(0)
        except ListEmptyError:
            print('Значение не получено. Список пуст.')

    def is_empty(self) -> bool:
        if len(self.queue_list):
            return True  # True - если пуст.
        else:
            return False

    def clear(self) -> None:
        self.queue_list.clear()

    def len(self) -> int:
        return len(self.queue_list)


a = Queue(5)  # Максимальное количество элементов в списке задач.
a.add('a')
a.add('b')
a.add('c')
a.add('b')
a.add('c')
a.add('c')
print(a.extract())
print(a.extract())
a.clear()
print(a.extract())
print(a.len())


