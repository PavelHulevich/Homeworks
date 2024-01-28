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
    def __init__(self, max_queue: int):
        self.max_queue = max_queue
        self.queue_list = []

    def add(self, str_in: str) -> None:
        try:
            if len(self.queue_list) >= self.max_queue:
                raise ListTooLongError
            print(f'\nДобавляем задачу: "{str_in}" в очередь')
            self.queue_list.append(str_in)
        except ListTooLongError:
            print(f'\nЗадача не добавлена. Список задач достиг максимального размера в {self.max_queue} элементов.')

    def extract(self) -> Optional[str]:
        # На выходе первая задача из списка, или "None" если список пуст.
        try:
            if not len(self.queue_list):
                raise ListEmptyError
            print(f'\nПолучаем задачу "{self.queue_list[0]}" из начала списка')
            str_out = self.queue_list.pop(0)
        except ListEmptyError:
            print('\nЗадача не получена. Список пуст.')
            str_out = None
        return str_out

    def is_empty(self) -> bool:
        if len(self.queue_list):
            is_empty_queue = True  # True - если пуст.
        else:
            is_empty_queue = False
        return is_empty_queue

    def clear(self) -> None:
        print('\nОчистка списка задач')
        self.queue_list.clear()

    def size(self) -> int:
        print('\nПолучение размера списка задач')
        return len(self.queue_list)


# Тестовые вызовы
a = Queue(5)  # Максимальное количество элементов в списке задач.
a.add('a')
print(a.queue_list)
a.add('b')
print(a.queue_list)
a.add('c')
print(a.queue_list)
a.add('b')
print(a.queue_list)
a.add('c')
print(a.queue_list)
a.add('c')
print(a.queue_list)
b = (a.extract())
print(a.queue_list)
b = (a.extract())
print(a.queue_list)
print(a.size())
a.clear()
print(a.queue_list)
b = (a.extract())
print(a.queue_list)
print(a.size())


