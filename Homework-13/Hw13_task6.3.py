"""Задание 6:
Создать data transfer object (DTO) для хранения и передачи информации о студенте. DTO
должен иметь следующие атрибуты: имя, фамилия, возраст, курс, средний балл. Реализовать
DTO с использованием четырех разных способов: dataclass, namedtuple, typeddict и pydantic.
Добавить валидацию полей с помощью аннотаций типов, проверок и исключений. Проверки:
• Имя и фамилия должны состоять только из букв английского алфавита и начинаться с
заглавной буквы
• Возраст должен быть не младше 18 и не старше 30
• Курс должен быть не меньше 1 и не больше 6
• Средний балл должен быть не больше 100 и не меньше 1"""
# DTO с использованием typeddict
from typing import TypedDict
ALPHABET = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALPHABET_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class StudentDTO(TypedDict):
    last_name: str
    first_name: str
    age: int
    course: int
    average_score: float


def is_alphabet(str_in: str) -> bool:
    alphabet_set = set(ALPHABET)
    str_in_set = set(str_in)
    return str_in_set == (str_in_set & alphabet_set)


def validate(student: dict) -> None:
    is_validate = True
    if not (18 <= student['age'] <= 30):
        is_validate = False
    if not (1 <= student['course'] <= 6):
        is_validate = False
    if not (1 <= student['average_score'] <= 100):
        is_validate = False
    if not is_alphabet(student['last_name']):
        is_validate = False
    if not is_alphabet(student['first_name']):
        is_validate = False
    if student['first_name'][0] not in ALPHABET_UPPER:
        is_validate = False
    if student['last_name'][0] not in ALPHABET_UPPER:
        is_validate = False
    if not is_validate:
        raise ValueError


first_name = 'John'
last_name = 'Doe'
age = 19
course = 1
average_score = 100

student = {'first_name': first_name, 'last_name': last_name, 'age': age, 'course': course, 'average_score': average_score}
try:
    validate(student)
except ValueError:
    print('Ошибка валидации')
else:
    user_dto = StudentDTO(student)
    print(user_dto)



