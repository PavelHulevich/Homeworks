"""Задание 5:
Создайте класс Book, который будет представлять книгу. Класс должен иметь атрибуты title,
author и pages, которые будут хранить название, автора и количество страниц книги. Также
создайте метод read, который будет принимать количество страниц, которые были прочитаны,
и возвращать процент прочтения книги. Затем создайте класс Library, который будет
представлять библиотеку. Класс должен иметь атрибут books, который будет хранить список
объектов класса Book, и метод add_book, который будет добавлять книгу в список.
"""
from typing import List
from faker import Faker


class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'Название: {self.title} Автор: {self.author}. Страниц: {self.pages}'

    def read(self, pages_number: int) -> int:
        return int(pages_number / self.pages * 100)


class Library:
    def __init__(self, books: List[Book]):
        self.books = books

    def add_book(self, book: Book) -> None:
        self.books.append(book)


fake = Faker('ru')
books_list = []
for i in range(5):
    books_list.append(Book(fake.sentence(nb_words=3), fake.last_name(), fake.random_int(50, 250)))
print(books_list[0])
print(f'Прочитано: 20 страниц, {books_list[0].read(20)} %')
library = Library([])
library.add_book(books_list[0])
library.add_book(books_list[1])
