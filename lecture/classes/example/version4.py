"""
Создадим класс, который имитирует выпивание напитка. Выпивать можно весь напиток сразу большими глотками или маленькими.
"""

# Добавим метод сделать глоток напитка. При каждом глотке объем напитка уменьшается, нельзя делать глоток
# если напитка нет


class Drink:
    volume = 200

    def __init__(self, name, price):
        self.name = name
        self.price = price

        # Устанавливаем начальное значение атрибута remains для хранения информации о том сколько напитка осталось
        self.remains = self.volume

    def drink_info(self):
        # Добавляем информацию об остатке напитка в метод drink_info.
        print(
            f'Название: {self.name}. Стоимость: {self.price}. Начальный объём: {self.volume}. Осталось: {self.remains}'
        )

    # Метод, чтобы сделать глоток 20 ml
    def make_drink(self):
        # Проверяем, достаточно ли напитка осталось.
        if self.remains >= 20:
            self.remains -= 20
            print('Глоток сделан')
        else:
            print('Не хватает напитка')


#  Создадим объект coffee — экземпляр класса Drink
coffee = Drink(name='Кофе', price=300)
coffee.drink_info()
coffee.make_drink()
coffee.drink_info()
coffee.make_drink()
coffee.drink_info()

#  Создадим объект tea — экземпляр класса Drink
tea = Drink(name='Чай', price=200)
tea.drink_info()
tea.make_drink()
tea.drink_info()
