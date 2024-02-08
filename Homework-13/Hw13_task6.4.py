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
# DTO с использованием pydantic
from pydantic import BaseModel, validator, ValidationError

ALPHABET = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALPHABET_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class StudentDTO(BaseModel):
    last_name: str
    first_name: str
    age: int
    course: int
    average_score: float

    @validator('age')
    def validate_age(cls, value: int) -> int:
        if 18 <= value <= 30:
            return value
        raise ValidationError

    @validator('course')
    def validate_course(cls, value: int) -> int:
        if 1 <= value <= 6:
            return value
        raise ValidationError

    @validator('average_score')
    def validate_average_score(cls, value: float) -> float:
        if 1 <= value <= 100:
            return value
        raise ValidationError

    @validator('last_name', 'first_name')
    def validate_names(cls, value: str) -> str:
        alphabet_set = set(ALPHABET)
        str_in_set = set(value)
        if str_in_set != (str_in_set & alphabet_set):
            raise ValueError
        if value[0] not in ALPHABET_UPPER:
            raise ValidationError
        return value


try:
    user_dto = StudentDTO(**{'first_name': 'John', 'last_name': 'Doe', 'age': 19, 'course': 1, 'average_score': 10})
except ValidationError:
    print('Ошибка валидации')
else:
    print(user_dto)

