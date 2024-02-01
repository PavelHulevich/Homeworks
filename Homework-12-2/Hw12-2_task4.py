"""Задание 4:
Создайте класс BankAccount, который будет представлять банковский счет. Класс должен
иметь атрибуты number, balance и owner, которые будут хранить номер счета, баланс и
владельца счета. Также создайте методы deposit, withdraw и transfer, которые будут позволять
вносить, снимать и переводить деньги с одного счета на другой. Затем создайте класс Person,
который будет представлять человека. Класс должен иметь атрибуты name, age и accounts,
которые будут хранить имя, возраст и список счетов человека. Также создайте метод
get_total_balance, который будет возвращать общий баланс по всем счетам человека."""
from __future__ import annotations
from typing import List


class BankAccount:
    def __init__(self, number: int, balance: float, owner: str):
        self.number = number
        self.balance = balance
        self.owner = owner

    def __str__(self):
        return f'{self.number}, {self.balance}, {self.owner}'

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        self.balance -= amount

    def transfer(self, to_account: BankAccount, amount: float) -> None:
        self.balance -= amount
        to_account.balance += amount


class Person:
    def __init__(self, name: str, age: int, accounts: List[BankAccount]):
        self.name = name
        self.age = age
        self.accounts = accounts

    def get_total_balance(self) -> float:
        summ = 0
        for account in self.accounts:
            summ += account.balance
        return summ


a = BankAccount(121, 50, 'Вася')
b = BankAccount(131, 70, 'Вася')
c = BankAccount(141, 80, 'Федя')

print(a)
print(b)
pa = Person('Вася', 27, [a, b])
print(pa.get_total_balance())

a.deposit(120)
print(a)
a.transfer(b, 20)
print(a, b)
