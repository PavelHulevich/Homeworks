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
        if not len(self.queue_list):
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

TEST_TUPLE = ('task_queue = Queue(5)', 'print(task_queue.queue_list)',
              'task_queue.add("a")',
              'task_queue.add("b")', 'print(task_queue.queue_list)',
              'task_queue.add(25)', 'print(task_queue.queue_list)',
              'task_queue.add({1, 2})', 'print(task_queue.queue_list)',
              'task_queue.add("e")', 'print(task_queue.queue_list)',
              'task_queue.add("e")', 'print(task_queue.queue_list)',
              'print(task_queue.extract())', 'print(task_queue.queue_list)',
              'print(task_queue.extract())', 'print(task_queue.queue_list)',
              'print(task_queue.size())', 'print(task_queue.queue_list)',
              'print(task_queue.is_empty())', 'print(task_queue.queue_list)',
              'task_queue.clear()', 'print(task_queue.queue_list)',
              'print(task_queue.is_empty())', 'print(task_queue.queue_list)',
              'print(task_queue.extract())', 'print(task_queue.queue_list)',)
for tupleCur in TEST_TUPLE:
    print(f'\nВыполняем команду: {tupleCur}')
    exec(tupleCur)
