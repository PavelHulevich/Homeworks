"""Задание 2:
Создайте класс Employee, который будет представлять сотрудника компании. Класс должен
иметь атрибуты name, position, salary и метод get_info, который возвращает строку с
информацией о сотруднике. Затем создайте класс Manager, который будет наследовать от
класса Employee и добавлять атрибут subordinates, который будет хранить список
подчиненных менеджера. Также переопределите метод get_info, чтобы он включал в строку
количество подчиненных. Кроме того, создайте метод add_subordinate, который будет
добавлять сотрудника в список подчиненных, и метод remove_subordinate, который будет
удалять сотрудника из списка подчиненных.
"""
from faker import Faker


class Employee:
    def __init__(self, name: str, position: str, salary: float):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self) -> str:
        return f'Имя: {self.name}. Должность: {self.position}. Зарплата: {self.salary}.'


class Manager(Employee):
    def __init__(self, name: str, position: str, salary: float):
        self.subordinates = []
        super().__init__(name, position, salary)

    def get_info(self) -> str:
        return (f'Имя: {self.name}. Должность: {self.position}.'
                f' Зарплата: {self.salary}. Подчиненных: {len(self.subordinates)}')

    def add_subordinates(self, new_subordinates: Employee) -> None:
        if new_subordinates not  in self.subordinates:
            self.subordinates.append(new_subordinates)
        else:
            print('Такой сотрудник уже есть в подчинении')

    def remove_subordinates(self, ex_subordinates: Employee) -> None:
        self.subordinates.remove(ex_subordinates)


fake = Faker('ru')
employs = [0 for _ in range(0, 10)]
managers = [0 for _ in range(0, 3)]
for i in range(10):
    employs[i] = Employee(fake.first_name(), fake.job(), fake.random_int(70, 300, 5))
    print(employs[i].get_info())
print()
for i in range(3):
    managers[i] = Manager(fake.first_name(), fake.job(), fake.random_int(100, 400, 10))
    print(managers[i].get_info())
print()
managers[0].add_subordinates(employs[0])
print(managers[0].get_info())

managers[0].add_subordinates(employs[0])
print(managers[0].get_info())

managers[0].add_subordinates(employs[1])
print(managers[0].get_info())
managers[0].remove_subordinates(employs[0])
print(managers[0].get_info())



