from abc import ABC

__all__ = (
    'CArmour',
    'HArmour',
    'SArmour',
)

from abc import abstractmethod

from ammo import *


class Armour(ABC):

    def __init__(self, thickness: int, armour_type: str):
        self.thickness = thickness
        self.armour_type = armour_type

    def is_penetrated(self, projectile: Ammo) -> bool:
        return projectile.get_damage() > self.thickness


class CArmour(Armour):

    def __init__(self, thickness: int):
        super().__init__(thickness, 'комбинированная')


class HArmour(Armour):

    def __init__(self, thickness: int):
        super().__init__(thickness, 'гомогенная')


class SArmour(Armour):

    def __init__(self, thickness: int):
        super().__init__(thickness, 'разнесенная')
