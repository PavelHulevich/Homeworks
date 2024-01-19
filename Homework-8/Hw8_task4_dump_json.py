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


class Student:  # Student card.
    def __init__(self, first, last, age, course, group, subject_score: dict):
        self.first = first
        self.last = last
        self.age = age
        self.course = course
        self.group = group
        self.subject_score = dict(subject_score)


def class_to_dict(obj_dict):  # for dump json-file.
    return obj_dict.__dict__


fake = Faker('ru')
subject_list = ['Устройство варп-двигателей', 'Пятимерное черчение',
                'Атомное конструирование ', 'Пипелацестроение']
group_list = ['Прикладная космонавтика', 'Машинное доение', 'Физика пустоты']
student_list = []
student_score = dict()

for i in range(0, 10):  # Создание объекта student_list (список) класса Студент.
    for j in subject_list:
        student_score[j] = randint(3, 10)
    student_list.append(Student(fake.first_name(), fake.last_name(), randint(18, 24),
                                randint(1, 5), group_list[randint(0, len(group_list) - 1)], student_score))

# Удаление старого файла json, если он есть, и запись нового с сериализацией объекта класса в словарь.
if os.path.isfile('student_list.json'):
    os.remove('student_list.json')
    print("Предыдущий файл с именем 'student_list.json' удален. Создаем новый.")
else:
    print("Файл 'student_list.json' не существует. Создаем новый")
with open('student_list.json', 'w') as outfile:
    json.dump(student_list, outfile, default=class_to_dict)
