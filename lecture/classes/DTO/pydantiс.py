"""
Библиотека Pydantic представляет собой инструмент для определения данных и конвертации данных в Python, который
использует аннотации типов для определения схемы данных и преобразует данные из JSON в объекты Python.

Может быть установлен с помощью команды pip install pydantic
"""

from pydantic import BaseModel, Field, validator, ValidationError

"""
Здесь мы определили модель UserDTO c базовой валидацией на длину строки и максимум возраста. 
Так же определили что данные для атрибута last_name будут приходить через параметр lastName.
"""


class UserDTO(BaseModel):
    first_name: str
    last_name: str = Field(min_length=2, alias="lastName")
    age: int = Field(lt=100, description="Age must be a positive integer")

    #  кастомнsq валидатор минимального возраста
    @validator('age')
    def validate_age(cls, value):
        if value < 18:
            raise ValueError

        return value


user_dto = UserDTO(**{'first_name': 'John', 'lastName': 'Doe', 'age': 19})
print(type(user_dto))

user_dto = UserDTO(first_name='John', lastName='Doe', age=20)
print(user_dto.dict())

try:
    UserDTO(**{'first_name': 'John', 'lastName': 'D', 'age': 3})
except ValidationError:
    pass
