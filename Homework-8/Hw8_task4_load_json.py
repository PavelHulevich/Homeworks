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
        if (not isinstance(dictionary['first'], str) or not isinstance(dictionary['last'], str) or
                not isinstance(dictionary['group'], str)):
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


def reading_json_file(name: str) -> list:
    # Чтение json-файла.
    with open(name) as infile:
        student_list_load_fn = json.load(infile)
    return student_list_load_fn


def deserialisation_and_setting_groups() -> None:
    # десериализация содержимого json-файла  в объект student_list_2 класса Student.
    for stud_card in student_list_load:
        student_list_2.append(Student(stud_card['first'], stud_card['last'], stud_card['age'], stud_card['course'],
                                      stud_card['group'], stud_card['subject_score']))
        groups_set.add(stud_card['group'])  # Создание множества из имеющихся групп.


def initialisation_groups_dicts() -> None:
    for group in groups_set:   # Словарь групп с ключами из множества, значения - нули.
        groups_dict[group] = 0  # Сумма средних балов студентов в группе.
        groups_dict_qnt[group] = 0  # Количество студентов в каждой отдельной группе.


def calculation_and_print_average_scores() -> None:
    all_score_sum = 0  # Сумма средних балов всех студентов.
    for obj in student_list_2:  # Вывод записей всех студентов.
        print(f'Студент:   {obj.first} {obj.last:}, возраст: {obj.age}, курс: {obj.course},'
              f' группа: {obj.group:18}\nОценки по предметам: {obj.subject_score}')

        score_sum = 0  # Сумма балов у каждого студента.
        for k, v in obj.subject_score.items():
            score_sum += v
        average_stud_score = score_sum / len(obj.subject_score)
        print(f'Средний бал ученика: {average_stud_score}\n')

        all_score_sum += average_stud_score
        groups_dict[obj.group] += average_stud_score
        groups_dict_qnt[obj.group] += 1

    for k, v in groups_dict.items():
        print(f'Средний бал в группе {k}: {v / groups_dict_qnt[k]:1.1f}')

    print(f'\nСредний бал всех учеников: {all_score_sum/len(student_list_2)}')


student_list_2 = []
groups_set = set()
groups_dict = dict()
groups_dict_qnt = dict()
json_file_name = 'student_list.json'

student_list_load = reading_json_file(json_file_name)  # Чтение json-файла.
validation_result = validate_enter_data(student_list_load)  # Проверка валидности входных данных.
if not validation_result:
    print('Входные данные не верны')
    exit()
deserialisation_and_setting_groups()
initialisation_groups_dicts()
calculation_and_print_average_scores()
