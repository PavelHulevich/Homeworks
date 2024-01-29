"""Задание 3:
Создайте класс поддерживающий сравнение объектов (>, >=, <, <=) разных типов данных (str,
int, list, dict). Для строк сравниваем количество букв, для цифр сравниваем количество
разрядов числа, для списков сравниваем количество элементов списка, для словарей
сравниваем сумму ключей и значений. Словари не могут быть вложенными. Класс должен
поддерживать сравнение перечисленных типов данных между собой.
"""


class Compare:

    def __init__(self, value):
        self.value = value

    def _get_length(self):
        weight = 0
        match self.value:
            case str() | list():
                weight = len(self.value)
            case dict():
                weight = len(self.value.keys()) * 2
            case int():
                weight = len(str(self.value))
        return weight

    def __gt__(self, other):
        if self._get_length() > other._get_length():
            return True
        else:
            return False

    def __lt__(self, other):
        if self._get_length() < other._get_length():
            return True
        else:
            return False

    def __le__(self, other):
        if self._get_length() <= other._get_length():
            return True
        else:
            return False

    def __ge__(self, other):
        if self._get_length() >= other._get_length():
            return True
        else:
            return False


d = Compare({'a': 1})
s = Compare('sty')
print(d >= s)
print(d <= s)
print(d > s)
print(d > s)




