"""
Dataclass - это декоратор, который предоставляет простой способ создания классов для хранения данных.
Dataclass использует аннотации типов для определения полей, а затем генерирует все методы, необходимые для создания и
использования объектов этого класса.
Для создания DTO с помощью dataclass нужно добавить декоратор dataclass и определить поля с аннотациями типов.
"""

from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import FrozenInstanceError


@dataclass
class UserDTO:
    last_name: str
    first_name: str = ''  # значение по умолчанию

    #  метод, добавленный декоратором dataclass в объект UserDTO
    #  позволяет выполнять валидацию данных
    def __post_init__(self):
        self.validate()

    def validate(self):
        if len(self.last_name) <= 2:
            raise ValueError


user_dto = UserDTO(**{'first_name': 'John', 'last_name': 'Doe'})
print(user_dto)

user_dto = UserDTO(first_name='John', last_name='Doe')
print(asdict(user_dto))  # метод asdict для выгрузки в словарь

user_dto = UserDTO(last_name='Doe')
print(asdict(user_dto))

try:
    user_dto = UserDTO(**{'first_name': 'John', 'last_name': 'Do'})
except ValueError:
    pass


# чтобы создать неизменяемый объект нужно в декаратор передавать аргумент frozen=True
@dataclass(frozen=True)
class UserDTO:
    first_name: str
    last_name: str = ''

    def __post_init__(self):
        self.validate()

    def validate(self):
        if len(self.last_name) <= 2:
            raise ValueError


user_dto = UserDTO(first_name='John', last_name='Doe')
try:
    user_dto.first_name = 'user_dto'
except FrozenInstanceError:
    pass
