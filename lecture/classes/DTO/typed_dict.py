"""
тип данных позволяет создавать словари с фиксированным набором ключей и аннотациями типов значений.
Такой подход делает TypedDict
"""
from typing import TypedDict


class UserDTO(TypedDict):
    first_name: str
    last_name: str


user_dto = UserDTO(**{'first_name': 'John', 'last_name': 'Doe'})

print(user_dto)
print(type(user_dto))

print(user_dto.keys())
print(user_dto.values())
