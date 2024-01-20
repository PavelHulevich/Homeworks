"""
Задание 4:
Напишите программу, которая читает json-файл, содержащий информацию о студентах (имя,
фамилия, возраст, курс, группа, предмет, оценка) и выводит на экран средний балл каждого
студента и общий средний балл по группе.
"""

from faker import Faker
from random import randint
import os
import json


class Student:  # Карточка студент
    def __init__(self, first: str, last: str, age: int, course: int, group: str, subject_score: dict):
        self.first = first
        self.last = last
        self.age = age
        self.course = course
        self.group = group
        self.subject_score = dict(subject_score)


def class_to_dict(obj_dict):  # Класс в словарь
    return obj_dict.__dict__


fake = Faker('ru')
subject_list = ['Устройство варп-двигателей', 'Пятимерное черчение',
                'Атомное конструирование ', 'Пипелацестроение']
group_list = ['Прикладная космонавтика', 'Машинное доение', 'Физика пустоты']
student_list = []
subject_score = dict()
student_qnt = 10    # Количество генерируемых студентов

for _ in range(0, student_qnt):  # Создание объекта student_list (список) класса Студент.
    for subject in subject_list:
        subject_score[subject] = randint(3, 10)  # Оценка по предмету генерируется
    student_list.append(Student(fake.first_name(), fake.last_name(), randint(18, 24),
                                randint(1, 5), group_list[randint(0, len(group_list) - 1)], subject_score))

# Удаление старого файла json, если он есть, и запись нового с сериализацией объекта класса в словарь.
if os.path.isfile('student_list.json'):
    os.remove('student_list.json')
    print("Предыдущий файл с именем 'student_list.json' удален. Создаем новый.")
else:
    print("Файл 'student_list.json' не существует. Создаем новый")
with open('student_list.json', 'w') as outfile:
    json.dump(student_list, outfile, default=class_to_dict)
print(f'JSON-файл с данными {student_qnt} студентов создан и сохранен под именем: "student_list.json"')
