from abc import ABC
from abc import abstractmethod
from gun import Gun


__all__ = (
    'Ammo',
    'APCartridge',
    'HECartridge',
    'HEATCartridge',
)


class Ammo(ABC):

    def __init__(self, gun: Gun, ammo_type: str):
        self.gun = gun
        self.ammo_type = ammo_type

    def get_damage(self) -> float:
        return self.gun.get_caliber() * 3

    def get_penetration(self):
        return self.gun.get_caliber()

    def __str__(self):
        return f'Снаряд {self.ammo_type} к пушке калибра {self.gun.get_caliber()}'


class APCartridge(Ammo):

    def __init__(self, gun: Gun):
        super().__init__(gun, 'подкалиберный')


class HECartridge(Ammo):

    def __init__(self, gun: Gun):
        super().__init__(gun, 'фугасный')


class HEATCartridge(Ammo):

    def __init__(self, gun: Gun):
        super().__init__(gun, 'кумулятивный')
