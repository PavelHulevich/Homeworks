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

    def __init__(self):
        super().__init__(ammo_type='подкалиберный')


class HECartridge(Ammo):

    def __init__(self):
        super().__init__(ammo_type='фугасный')


class HEATCartridge(Ammo):

    def __init__(self):
        super().__init__(ammo_type='кумулятивный')
