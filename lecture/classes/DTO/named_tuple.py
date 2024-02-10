"""
NamedTuple - это класс из стандартной библиотеки Python, который представляет собой неизменяемый кортеж с
доступом к свойствам по имени. Встроенной валидации типов и данных нет.
"""

from typing import NamedTuple


class UserDTO(NamedTuple):
    first_name: str
    last_name: str


user_dto = UserDTO(**{'first_name': 'John', 'last_name': 'Doe'})
print(user_dto.first_name)

print(user_dto)
print(user_dto._asdict())

try:
    user_dto.first_name = 'Bill'
except AttributeError:
    pass

user_dto = UserDTO(**{'first_name': 1, 'last_name': 'Doe'})
print(user_dto._asdict())
