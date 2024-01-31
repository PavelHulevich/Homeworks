class Gun:

    def __init__(self, caliber: int, barrel_length: int):
        self.caliber = caliber
        self.barrel_length = barrel_length

    def is_on_target(self, dice: int) -> bool:
        # трешхолд для пушки - величина, выше которой будем считать, что снаряд попал в цель

        print(self.barrel_length + dice)
        return (self.barrel_length + dice) > 100
