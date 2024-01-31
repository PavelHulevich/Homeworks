"""
Создадим класс, который имитирует выпивание напитка. Выпивать можно весь напиток сразу большими глотками или маленькими.
"""

# Уберем дублирование логики, введем защищенный метод


class Drink:
    volume = 200

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.remains = self.volume

    def drink_info(self):
        print(
            f'Название: {self.name}. Стоимость: {self.price}. Начальный объём: {self.volume}. Осталось: {self.remains}'
        )

    def _is_enough(self, need):
        if self.remains >= need and self.remains > 0:
            return True

        print('Недостаточно напитка')
        return False

    def make_drink(self):
        if self._is_enough(20) == True:
            self.remains -= 20
            print('Глоток сделан')

    def make_small_drink(self):
        if self._is_enough(10) == True:
            self.remains -= 10
            print('Глоток сделан')

    def drink_all(self):
        if self._is_enough(0) == True:
            self.remains = 0
            print('Глоток сделан')


#  Создадим объект coffee — экземпляр класса Drink
coffee = Drink(name='Кофе', price=300)
coffee.drink_info()
coffee.make_drink()
coffee.drink_info()
coffee.make_small_drink()
coffee.drink_info()
coffee.drink_all()
coffee.drink_info()
coffee.make_small_drink()

#  Создадим объект tea — экземпляр класса Drink
tea = Drink(name='Чай', price=200)
tea.drink_info()
tea.make_drink()
tea.drink_info()
