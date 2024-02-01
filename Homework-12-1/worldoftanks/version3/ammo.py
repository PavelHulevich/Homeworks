from abc import ABC


__all__ = (
    'APCartridge',
    'HECartridge',
    'HEATCartridge',
)


class Ammo(ABC):

    def __init__(self, ammo_type: str):
        self.ammo_type = ammo_type


class APCartridge(Ammo):
    pass


class HECartridge(Ammo):
    pass


class HEATCartridge(Ammo):
    pass
