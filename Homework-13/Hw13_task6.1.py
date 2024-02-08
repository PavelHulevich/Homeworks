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
# DTO с использованием dataclass
from dataclasses import asdict, dataclass


@dataclass
class StudentDTO:
    last_name: str
    first_name: str
    age: int
    course: int
    average_score: float
    ALPHABET = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ALPHABET_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __post_init__(self):
        self.validate()

    def validate(self):
        is_validate = True
        if not (18 <= self.age <= 30):
            is_validate = False
        if not (1 <= self.course <= 6):
            is_validate = False
        if not (1 <= self.average_score <= 100):
            is_validate = False
        if not self.is_upper(self.last_name):
            is_validate = False
        if not self.is_upper(self.first_name):
            is_validate = False
        if self.first_name[0] not in self.ALPHABET_UPPER:
            is_validate = False
        if self.last_name[0] not in self.ALPHABET_UPPER:
            is_validate = False
        if not is_validate:
            raise ValueError

    def is_upper(self, str_in) -> bool:
        alphabet_set = set(self.ALPHABET)
        str_in_set = set(str_in)
        return str_in_set == (str_in_set & alphabet_set)

try:
    user_dto = StudentDTO(**{'first_name': 'John', 'last_name': 'Doe', 'age': 19, 'course': 1, 'average_score': 100})
except ValueError:
    print('Ошибка валидации')
else:
    print(user_dto)
    print(asdict(user_dto))





