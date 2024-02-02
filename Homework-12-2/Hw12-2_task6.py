"""Задание 6:
Создайте класс Product, который будет представлять товар в интернет-магазине. Класс
должен иметь атрибуты name, price и description, которые будут хранить название, цену и
описание товара. Затем создайте класс Cart, который будет представлять корзину покупателя.
Класс должен иметь атрибут items, который будет хранить список объектов класса Product, и
методы add_item, remove_item и get_total, которые будут добавлять, удалять и возвращать
общую стоимость товаров в корзине."""
from typing import List
from faker import Faker


class Product:
    def __init__(self, name: str, price: float, description: str):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f'Название: {self.name}  Цена: {self.price}  Описание: {self.description}'


class Cart:
    def __init__(self, items: List[Product]):
        self.items = items

    def add_item(self, item: Product) -> None:
        self.items.append(item)

    def remove_item(self, item: Product) -> None:
        self.items.remove(item)

    def get_total(self) -> float:
        total = 0
        for prod in self.items:
            total += prod.price
        return total


fake = Faker('ru')
product_list = []
for i in range(5):
    product_list.append(Product(fake.sentence(nb_words=1), fake.random_int(50, 250), fake.sentence(nb_words=3)))
    print(product_list[i])

buyer_1 = Cart([])
buyer_1.add_item(product_list[3])
buyer_1.add_item(product_list[4])
print(f'\nОбщая цена покупки: {buyer_1.get_total()}')
buyer_1.remove_item(product_list[3])
print(f'\nОбщая цена покупки: {buyer_1.get_total()}')
