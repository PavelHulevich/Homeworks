class UserDTO:

    def __init__(self, **kwargs):
        self.first_name = kwargs.get("first_name")
        self.last_name = kwargs.get("last_name")
        self.validate_lastname()

    def to_dict(self):
        return self.__dict__

    def __repr__(self):
        return "I'm UserDTO"

    @classmethod
    def from_dict(cls, dict_obj):
        return cls(**dict_obj)

    def validate_lastname(self):
        if len(self.last_name) <= 2:
            raise ValueError("last_name length must be more then 2")


user_dto = UserDTO(first_name='John', last_name='Doe')
print(user_dto.to_dict())

user_dto = UserDTO.from_dict({'first_name': 'John', 'last_name': 'Doe'})
print(user_dto.to_dict())

print(user_dto)

try:
    user_dto = UserDTO.from_dict({'first_name': 'John', 'last_name': 'Do'})
except ValueError:
    pass
