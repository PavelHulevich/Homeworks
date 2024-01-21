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


def generation_student_class(student_qnt: int):
    for _ in range(0, student_qnt):  # Создание объекта student_list (список) класса Студент.
        for subject in subject_list:
            subject_score[subject] = randint(3, 10)  # Оценка по предмету генерируется

        student_list.append(Student(fake.first_name(), fake.last_name(), randint(18, 24),
                                    randint(1, 5), group_list[randint(0, len(group_list) - 1)], subject_score))

def writing_json_file(name_file, student_list_out):
    # Удаление старого файла json, если он есть, и запись нового с сериализацией объекта класса в словарь.
    if os.path.isfile(name_file):
        os.remove(name_file)
        print(f'Предыдущий файл с именем "{name_file}" удален. Создаем новый.')
    else:
        print(f"Файл {name_file} не существует. Создаем новый")
    with open(name_file, 'w') as outfile:
        json.dump(student_list_out, outfile, default=class_to_dict)
    print('JSON-файл с данными студентов создан и сохранен под именем: "student_list.json"')


fake = Faker('ru')
subject_list = ['Устройство варп-двигателей', 'Пятимерное черчение', 'Атомное конструирование ', 'Пипелацестроение']
group_list = ['Прикладная космонавтика', 'Машинное доение', 'Физика пустоты']
student_list = []
subject_score = dict()
student_quantity = 20    # Количество генерируемых студентов
file_out = 'student_list.json'

generation_student_class(student_quantity)
writing_json_file(file_out, student_list)


