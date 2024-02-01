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

    @abstractmethod
    def is_penetrated(self, projectile: Ammo) -> bool:
        return projectile.get_damage() > self.thickness


class CArmour(Armour):

    def __init__(self, thickness: int):
        super().__init__(thickness, 'комбинированная')

    def is_penetrated(self, projectile: Ammo) -> bool:
        print(f'Прилетел снаряд {projectile.ammo_type} калибра {projectile.get_penetration()}')

        if isinstance(projectile, HECartridge):
            print(f'Броня = {self.thickness * 1.0}мм')
            return projectile.get_penetration() > self.thickness * 1.0

        elif isinstance(projectile, HEATCartridge):
            print(f'Броня = {self.thickness * 0.8}мм')
            return projectile.get_penetration() > self.thickness * 0.8

        else:
            print(f'Броня = {self.thickness * 1.2}мм')
            return projectile.get_penetration() > self.thickness * 1.2


class HArmour(Armour):

    def __init__(self, thickness: int):
        super().__init__(thickness, 'гомогенная')

    def is_penetrated(self, projectile: Ammo) -> bool:
        print(f'Прилетел снаряд {projectile.ammo_type} калибра {projectile.get_penetration()}')

        if isinstance(projectile, HECartridge):
            # Если фугасный, то толщина брони считается больше
            print(f'Броня = {self.thickness * 1.2}мм')
            return projectile.get_penetration() > self.thickness * 1.2

        elif isinstance(projectile, HEATCartridge):
            print(f'Броня = {self.thickness * 1.0}мм')
            return projectile.get_penetration() > self.thickness * 1.0

        else:
            print(f'Броня = {self.thickness * 0.7}мм')
            return projectile.get_penetration() > self.thickness * 0.7


class SArmour(Armour):

    def __init__(self, thickness: int):
        super().__init__(thickness, 'разнесенная')

    def is_penetrated(self, projectile: Ammo) -> bool:
        print(f'Прилетел снаряд {projectile.ammo_type} калибра {projectile.get_penetration()}')

        if isinstance(projectile, HECartridge):
            # Если фугасный, то толщина брони считается меньше
            print(f'Броня = {self.thickness * 0.8}мм')
            return projectile.get_penetration() > self.thickness * 0.8

        elif isinstance(projectile, HEATCartridge):
            # Если кумулятивный, то толщина брони как бы больше
            print(f'Броня = {self.thickness * 1.2}мм')
            return projectile.get_penetration() > self.thickness * 1.2

        else:
            print(f'Броня = {self.thickness * 1.0}мм')
            return projectile.get_penetration() > self.thickness * 1.0
