"""Задание 2:
Предположим, у нас есть класс Employee, который хранит информацию о сотруднике и его
зарплате. Класс имеет метод calculate_salary(), который вычисляет зарплату сотрудника в
зависимости от его типа: менеджер, разработчик, тестировщик и т.д. Метод выглядит
примерно так:
class Employee:

 def __init__(self, name, type, base_salary):
 self.name = name
 self.type = type
 self.base_salary = base_salary

 def calculate_salary(self):
 bonus = 0
 if self.type == "manager":
 bonus = self.base_salary * 0.2
 elif self.type == "developer":
 bonus = self.base_salary * 0.1
 elif self.type == "tester":
 bonus = self.base_salary * 0.3
 return self.base_salary + bonus
Этот класс нарушает принцип OCP, потому что если мы захотим добавить новый тип
сотрудника или изменить правила расчета бонусов, нам придется изменить код метода
calculateSalary(). Это может привести к ошибкам, сложности тестирования и нарушению
работы существующего кода, который использует этот класс.
Чтобы исправить эту проблему необходимо сделать следующее:
• Создать абстрактный класс Employee, который будет содержать общие поля и методы для
всех сотрудников, а также абстрактный метод calculate_salary(), который будет
переопределяться в подклассах.
• Создать подклассы Manager, Developer и Tester, которые будут наследоваться от класса
Employee и реализовывать метод calculate_salary() в соответствии с их логикой расчета
бонусов."""
from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, type: str):
        self.type = type

    @abstractmethod
    def calculate_salary(self):
        ...


class Manager(Employee):
    def __init__(self, name: str, base_salary: float):
        super().__init__('manager')
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self) -> float:
        return self.base_salary * 1.2


class Developer(Employee):
    def __init__(self, name: str, base_salary: float):
        super().__init__('manager')
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self) -> float:
        return self.base_salary * 1.1


class Tester(Employee):
    def __init__(self, name: str, base_salary: float):
        super().__init__('manager')
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self) -> float:
        return self.base_salary * 1.3
