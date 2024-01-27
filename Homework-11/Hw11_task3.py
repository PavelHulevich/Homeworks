"""Задание 3:
Cоздайте класс поддерживающий сравнение объектов (>, >=, <, <=) разных типов данных (str,
int, list, dict). Для строк сравниваем количество букв, для цифр сравниваем количество
разрядов числа, для списков сравниваем количество элементов списка, для словарей
сравниваем сумму ключей и значений. Словари не могут быть вложенными. Класс должен
поддерживать сравнение перечисленных типов данных между собой.
"""


class Compare:
    def __init__(self):
        self.operation = ''
        self.val_weight = 0
        self.val1_weight = 0
        self.val2_weight = 0
        self.val = 0
        self.val1 = 0
        self.val2 = 0

    def compare_out(self, val1, operation, val2):
        self.val1 = val1
        self.val2 = val2
        self.operation = operation
        self.val1_weight = self.vals_weight(val1)
        self.val2_weight = self.vals_weight(val2)
        match self.operation:
            case '>':
                if self.val1_weight > self.val2_weight:
                    return self.it_true_false(True)
            case '<':
                if self.val1_weight < self.val2_weight:
                    return self.it_true_false(True)
            case '>=':
                if self.val1_weight >= self.val2_weight:
                    return self.it_true_false(True)
            case '<=':
                if self.val1_weight <= self.val2_weight:
                    return self.it_true_false(True)
        return self.it_true_false(False)

    def it_true_false(self, flag):
        if flag:
            return f'{str(self.val1)} {self.operation} {str(self.val2)} - Истинно'
        else:
            return f'{str(self.val1)} {self.operation} {str(self.val2)} - Ложно'

    def vals_weight(self, val) -> int:
        self.val = val
        match self.val:
            case str():
                self.val_weight = len(self.val)
            case list():
                self.val_weight = len(self.val)
            case int():
                self.val_weight = len(str(self.val))
            case dict():
                self.val_weight = len(list(self.val.keys()) + list(self.val.values()))
        return self.val_weight


a = Compare()
print(a.compare_out({'foo': 'bar', 'foo1': 'bar1'}, '<', 353))