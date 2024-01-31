"""
Создадим класс, который имитирует выпивание напитка. Выпивать можно весь напиток сразу большими глотками или маленькими.
"""

# Добавим метод получения информации о напитке


class Drink:
    volume = 200

    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Метод, чтобы получения информацию о напитке.
    def drink_info(self):
        print(f'Название: {self.name}. Стоимость: {self.price}. Объём: {self.volume}')


#  Создадим объект coffee — экземпляр класса Drink
coffee = Drink(name='Кофе', price=300)
coffee.drink_info()

#  Создадим объект tea — экземпляр класса Drink
tea = Drink(name='Чай', price=200)
tea.drink_info()
