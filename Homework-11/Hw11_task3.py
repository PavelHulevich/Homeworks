"""Задание 3:
Создайте класс поддерживающий сравнение объектов (>, >=, <, <=) разных типов данных (str,
int, list, dict). Для строк сравниваем количество букв, для цифр сравниваем количество
разрядов числа, для списков сравниваем количество элементов списка, для словарей
сравниваем сумму ключей и значений. Словари не могут быть вложенными. Класс должен
поддерживать сравнение перечисленных типов данных между собой.
"""
from typing import Union, Optional


class Compare:
    OPERATION_CHAR = ('<', '>', '<=', '>=')

    def __init__(self):
        self.operation = ''
        self.val_weight = 0
        self.val1_weight = 0
        self.val2_weight = 0
        self.val = 0
        self.val1 = 0
        self.val2 = 0

    def is_validate(self, val1: Union[str, list, dict, int], operation: str,
                    val2: Union[str, list, dict, int]) -> bool:
        # Валидация входных данных.
        is_not_error = True  # Флаг ошибки входных данных. По умолчанию "Истина" - ошибок нет.
        if not isinstance(val1, (int, str, list, dict)) or not isinstance(val2, (int, str, list, dict)):
            print('Ошибка. Один или оба операнда имеют недопустимый тип данных')
            is_not_error = False
        if not isinstance(operation, str):
            print('Ошибка. Знак операции сравнения имеет несимвольный тип.')
            is_not_error = False
        if operation not in self.OPERATION_CHAR:
            print('Ошибка. Недопустимый символ операции')
            is_not_error = False
        return is_not_error

    def vals_weight(self, val: Union[str, list, dict, int]) -> int:
        # Вычисляет вес переменной в зависимости от ее типа и установленных в задании правил.
        val_weight = 0
        match val:
            case str():
                val_weight = len(val)
            case list():
                val_weight = len(val)
            case int():
                val_weight = len(str(val))
            case dict():
                val_weight = len(list(val.keys()) + list(val.values()))
        return val_weight

    def comparing_main(self, val1, operation, val2):
        val1_weight = self.vals_weight(val1)
        val2_weight = self.vals_weight(val2)
        print(f'Выражение: {str(val1)} {operation} {str(val2)}', end='')
        compare_result = False
        match operation:
            case '>':
                if val1_weight > val2_weight:
                    compare_result = True
            case '<':
                if val1_weight < val2_weight:
                    compare_result = True
            case '>=':
                if val1_weight >= val2_weight:
                    compare_result = True
            case '<=':
                if val1_weight <= val2_weight:
                    compare_result = True
        if compare_result:
            print(' -- Истинно')
        else:
            print(' -- Ложно')
        return compare_result

    def comparing(self, val1: Union[str, list, dict, int], operation: str,
                  val2: Union[str, list, dict, int]) -> Optional[bool]:
        self.val1 = val1
        self.val2 = val2
        self.operation = operation

        print(f'\nПервый операнд:  {self.val1}. Операция:  "{self.operation}". Второй операнд:  {self.val2}.')
        if not self.is_validate(val1, operation, val2):
            print('Входные данные не верны')
            compare_result = None
        else:
            compare_result = self.comparing_main(val1, operation, val2)
        return compare_result


a = Compare()
print(a.comparing({'foo': 'bar', 'foo1': 'bar1'}, '>', 353))
