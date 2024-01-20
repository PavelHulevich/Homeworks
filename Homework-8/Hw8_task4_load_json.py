"""
Задание 4:
Напишите программу, которая читает json-файл, содержащий информацию о студентах (имя,
фамилия, возраст, курс, группа, предмет, оценка) и выводит на экран средний балл каждого
студента и общий средний балл по группе.
"""

import json


class Student:  # Student card.
    def __init__(self, first: str, last: str, age: int, course: int, group: str, subject_score: dict):
        self.first = first
        self.last = last
        self.age = age
        self.course = course
        self.group = group
        self.subject_score = dict(subject_score)


def validate_enter_data(list_in: list[dict]) -> bool:
    if not isinstance(list_in, list):
        print('Ошибка. На входе не список')
        return False
    for dictionary in list_in:
        if not isinstance(dictionary, dict):
            print('Ошибка. В списке не словари')
            return False
        for k, v in dictionary.items():
            if k not in ['first', 'last', 'age', 'course', 'group', 'subject_score']:
                print('Ошибка. В словаре неправильные ключи')
                return False
        if not isinstance(dictionary['first'], str) or not isinstance(dictionary['last'], str) or not isinstance(dictionary['group'], str):
            print('Ошибка. Значения словаря не строки')
            return False
        if not isinstance(dictionary['age'], int) or not isinstance(dictionary['course'], int):
            print('Ошибка. Значения словаря не целые числа')
            return False
        if not isinstance(dictionary['subject_score'], dict):
            print('Ошибка. Список предметов и оценок не словарь')
        for k, v in dictionary['subject_score'].items():
            if not isinstance(k, str) or not isinstance(v, int):
                print('Ошибка. Данные в словаре предметов и оценок не верны')
                return False
    return True


student_list_2 = []
group_set = set()
group_dict = dict()
group_dict_qnt = dict()

# Чтение json-файла. десериализация его содержимого в объект student_list_2 класса Student.
with open('student_list.json') as infile:
    student_list_load = json.load(infile)
print(student_list_load)

# Проверка валидности входных данных
validation_result = validate_enter_data(student_list_load)
if not validation_result:
    print('Входные данные не верны')
    exit()

# десериализация содержимого json-файла  в объект student_list_2 класса Student.
for stud_card in student_list_load:
    student_list_2.append(Student(stud_card['first'], stud_card['last'], stud_card['age'], stud_card['course'],
                                  stud_card['group'], stud_card['subject_score']))
    group_set.add(stud_card['group'])  # Множество имеющихся групп.

for group in group_set:   # Словарь групп с ключами из множества, значения - нули.
    group_dict[group] = 0  # Сумма средних балов студентов в группе
    group_dict_qnt[group] = 0  # Количество студентов в группе

all_score_sum = 0  # Сумма средних балов всех студентов.
for obj in student_list_2:  # Вывод записей всех студентов.
    print(f'Студент:   {obj.first} {obj.last:13}, возраст: {obj.age:3}, курс: {obj.course:2}, группа: {obj.group:18}\n'
          f'Оценки по предметам: {obj.subject_score}')

    score_sum = 0  # Сумма балов у каждого студента.
    for k, v in obj.subject_score.items():
        score_sum += v
    average_stud_score = score_sum / len(obj.subject_score)
    print(f'Средний бал ученика: {average_stud_score}\n')

    all_score_sum += average_stud_score
    group_dict[obj.group] += average_stud_score
    group_dict_qnt[obj.group] += 1

for k, v in group_dict.items():
    print(f'Средний бал в группе {k}: {v / group_dict_qnt[k]:1.1f}')

print(f'\nСредний бал всех учеников: {all_score_sum/len(student_list_2)}')



