from gun import Gun
from ammo import *


class Panzer:

    def __init__(self, model: str, gun: Gun, armour_thickness: int, health: int):
        self.model = model
        self.gun = gun
        self.armour_thickness = armour_thickness
        self.health = health

        self.ammos = []
        self.armours = []

        self.__load_ammos()

        self.selected_armour = 0
        self.loaded_ammo = None

    def __str__(self):
        return (f'Танк {self.model}; Здоровье = {self.health}; Заряженный снаряд: {self.loaded_ammo.ammo_type};')

    def __load_ammos(self):
        for i in range(10):
            self.ammos.append(APCartridge())
            self.ammos.append(HEATCartridge())
            self.ammos.append(HECartridge())

    def load_gun(self, ammo_type: str):
        for ammo in self.ammos:
            if ammo.ammo_type == ammo_type:
                self.loaded_ammo = ammo
                print('Заряжено!')
                return
