from gun import Gun
from ammo import *
from armour import *


class Panzer:

    def __init__(self, model: str, gun: Gun, armour_thickness: int, health: int):
        self.model = model
        self.gun = gun
        self.armour_thickness = armour_thickness
        self.health = health

        self.ammos = []
        self.armours = []

        self.__load_ammos()
        self.__add_armours()

        self.selected_armour = self.armours[0]
        self.loaded_ammo = None

    def __str__(self):
        return (f'Танк {self.model}; Здоровье = {self.health}; Заряженный снаряд: {self.loaded_ammo.ammo_type}; Выбранная броня: {self.selected_armour.armour_type}')

    def __load_ammos(self):
        for i in range(10):
            self.ammos.append(APCartridge())
            self.ammos.append(HEATCartridge())
            self.ammos.append(HECartridge())

    def __add_armours(self):
        self.armours.append(SArmour())
        self.armours.append(HArmour())
        self.armours.append(CArmour())

    def load_gun(self, ammo_type: str):
        for ammo in self.ammos:
            if ammo.ammo_type == ammo_type:
                self.loaded_ammo = ammo
                print('Заряжено!')
                return

    def select_armour(self, armour_type: str):
        for armour in self.armours:
            if armour.armour_type == armour_type:
                self.selected_armour = armour
                break
