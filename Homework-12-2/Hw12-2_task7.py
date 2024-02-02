"""Задание 7:
Создайте класс Student, который будет представлять студента университета. Класс должен
иметь атрибуты name, age и courses, которые будут хранить имя, возраст и список курсов
студента. Затем создайте класс Course, который будет представлять учебный курс. Класс
должен иметь атрибуты title, instructor и students, которые будут хранить название,
преподавателя и список студентов, записанных на курс. Также создайте метод enroll, который
будет принимать объект класса Student и добавлять его в список студентов курса, а также
добавлять курс в список курсов студента."""
from __future__ import annotations
from typing import List


class Student:
    def __init__(self, name: str, age: int, courses: List[Course]):
        self.name = name
        self.age = age
        self.courses = courses

    def __str__(self):
        return f'Имя: {self.name} Возраст: {self.age}'

    def print_stud(self):
        print(f'Имя: {self.name} Возраст: {self.age} Курсы: ')
        for i in self.courses:
            print(i)


class Course:
    def __init__(self, title: str, instructor: str, students: List[Student]):
        self.title = title
        self.instructor = instructor
        self.students = students

    def __str__(self):
        return f'Название: {self.title} Препод: {self.instructor}'

    def print_course(self):
        print(f'Название: {self.title} Препод: {self.instructor}')
        for i in self.students:
            print(i)

    def enroll(self, stud: Student) -> None:
        self.students.append(stud)
        stud.courses.append(self)


stud_1 = Student('Rick', 20, [])
stud_2 = Student('Nick', 21, [])
stud_3 = Student('Mack', 22, [])

cours_1 = Course('Природа', 'Валера', [])
cours_2 = Course('Вязание', 'Коля', [])
cours_3 = Course('Плавание', 'Миша', [])

cours_2.enroll(stud_1)
cours_2.enroll(stud_2)


stud_1.print_stud()
stud_2.print_stud()
stud_3.print_stud()
print()
cours_1.print_course()
cours_2.print_course()
cours_3.print_course()