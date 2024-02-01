import random

from gun import Gun
from ammo import *
from armour import *
from ammo import Ammo


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
            self.ammos.append(APCartridge(self.gun))
            self.ammos.append(HEATCartridge(self.gun))
            self.ammos.append(HECartridge(self.gun))

    def __add_armours(self):
        self.armours.append(SArmour(thickness=self.armour_thickness))
        self.armours.append(HArmour(thickness=self.armour_thickness))
        self.armours.append(CArmour(thickness=self.armour_thickness))

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

    def shoot(self):
        if self.loaded_ammo is None:
            print('не заряжено')
            return

        fired_ammo = self.ammos.pop(0)
        print(f'Танк {self.model} выстрелил {self.loaded_ammo.ammo_type} снаряд......')

        self.loaded_ammo = None

        dice = random.randint(0, 100)

        print(dice)
        if self.gun.is_on_target(dice):
            print('Попадание!')
            return fired_ammo
        else:
            print('Промах!')
            return None

    def handle_hit(self, projectile: Ammo):
        if self.selected_armour.is_penetrated(projectile):
            self.health -= projectile.get_damage()
        else:
            print('Броня не пробита.')

    def get_health(self):
        return self.health
