"""Задание 3:
Создайте класс поддерживающий сравнение объектов (>, >=, <, <=) разных типов данных (str,
int, list, dict). Для строк сравниваем количество букв, для цифр сравниваем количество
разрядов числа, для списков сравниваем количество элементов списка, для словарей
сравниваем сумму ключей и значений. Словари не могут быть вложенными. Класс должен
поддерживать сравнение перечисленных типов данных между собой.
"""
from typing import Union, Optional
from random import choice


class Compare:
    OPERATION_CHAR = ('<', '>', '<=', '>=')

    def is_validate(self, val1: Union[str, list, dict, int], operation: Union[str],
                    val2: Union[str, list, dict, int]) -> bool:
        # Валидация входных данных.
        is_not_error = True  # Флаг отсутствия ошибки входных данных. По умолчанию "Истина" - ошибок нет.
        if not isinstance(val1, (int, str, list, dict)) or not isinstance(val2, (int, str, list, dict)):
            print('Ошибка. Один или оба операнда имеют недопустимый тип данных')
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

    def comparing_statement(self, val1: Union[str, list, dict, int], operation: str,
                            val2: Union[str, list, dict, int]) -> bool:
        # Анализ логического утверждения. Сначала вызов вычисления веса переменных, затем сравнение.
        val1_weight = self.vals_weight(val1)  # Вес переменной_1.
        val2_weight = self.vals_weight(val2)  # Вес переменной_2.
        print(f'Выражение: {str(val1)} {operation} {str(val2)}', end='')
        is_statement_true = False  # Флаг результата сравнения. По умолчанию - "Ложь".
        match operation:
            case '>':
                if val1_weight > val2_weight:
                    is_statement_true = True
            case '<':
                if val1_weight < val2_weight:
                    is_statement_true = True
            case '>=':
                if val1_weight >= val2_weight:
                    is_statement_true = True
            case '<=':
                if val1_weight <= val2_weight:
                    is_statement_true = True
        if is_statement_true:
            print(' -- Истинно')
        else:
            print(' -- Ложно')
        return is_statement_true

    def comparing(self, val1: Union[str, list, dict, int], operation: Union[str],
                  val2: Union[str, list, dict, int]) -> Optional[bool]:
        # Главная функция, вызываемая экземпляром класса с параметрами.
        print(f'\nПервый операнд:  {val1}. Операция:  "{operation}". Второй операнд:  {val2}.')
        if not self.is_validate(val1, operation, val2):  # Проверка валидности данных
            print('Входные данные не верны')
            compare_result = None   # Если валидация не пройдена.
        else:
            compare_result = self.comparing_statement(val1, operation, val2)  # Если валидация пройдена
        return compare_result  # На выходе или bool или None:  -> Optional[bool]


# Тестовые прогоны
TEST_TUPLE = ({'foo': 'bar', 'foo1': 'bar1'}, 388, 44, [45, 85, 3], [25, 75], (45, 85, 66), 'say', 'else')
TEST_OPERATION_CHAR = ('<', '>', '<=', '>=', 'a', 25, [1, 2], 75, 4)

logical_expression = Compare()
for _ in range(0, 20):
    b = (logical_expression.comparing(choice(TEST_TUPLE), choice(TEST_OPERATION_CHAR), choice(TEST_TUPLE)))
    print('Результат возвращенный методом класса: ', b)
