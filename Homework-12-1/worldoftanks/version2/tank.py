from gun import Gun


class Panzer:

    def __init__(self, model: str, gun: Gun, armour_thickness: int, health: int):
        self.model = model
        self.gun = gun
        self.armour_thickness = armour_thickness
        self.health = health

        self.ammos = []
        self.armours = []

        self.selected_armour = 0
        self.loaded_ammo = None
