"""
Attr, работает точно так же как и dataclass
можно установить с помощью команды pip install attrs
"""

import attr


@attr.s
class UserDTO:
    first_name: str = attr.ib(
        default='John',  # значение по умолчанию
        validator=attr.validators.instance_of(str)  # валидация
    )
    last_name: str = attr.ib(default='Doe', validator=attr.validators.instance_of(str))


user_dto = UserDTO(first_name='John', last_name='Doe')
print(user_dto)

try:
    UserDTO(**{'first_name': 1, 'last_name': 'Doe'})
except TypeError:
    pass


#  Объект DTO можно также сделать неизменяемым с помощью аттрибута декоратора frozen=True.
@attr.s(frozen=True)
class UserDTO:
    first_name: str = attr.ib(default='John', validator=attr.validators.instance_of(str))
    last_name: str = attr.ib(default='Doe', validator=attr.validators.instance_of(str))


user_dto = UserDTO(first_name='John', last_name='Doe')
print(user_dto)

try:
    user_dto.first_name = 'sdfsdf'
except attr.exceptions.FrozenInstanceError:
    pass
