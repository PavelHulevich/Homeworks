from abc import ABC

__all__ = (
    'CArmour',
    'HArmour',
    'SArmour',
)


class Armour(ABC):

    def __init__(self, armour_type: str):
        self.armour_type = armour_type


class CArmour(Armour):

    def __init__(self):
        super().__init__('комбинированная')


class HArmour(Armour):

    def __init__(self):
        super().__init__('гомогенная')


class SArmour(Armour):

    def __init__(self):
        super().__init__('разнесенная')
