"""
Любой объект может реализовать методы встроенных последовательностей (словари, кортежи, списки, строки и так далее).
Доступ к значениям последовательности переопределяется следующими методами:
__len__(self) — вызывается методом len(...) и возвращает количество элементов в последовательности.
__getitem__(self, key) — вызывается при обращении к элементу в последовательности по его ключу (индексу).
                         Метод должен выбрасывать исключение TypeError, если используется некорректный тип ключа,
                        KeyError, если данному ключу не соответствует ни один элемент в последовательности
dict_object = {"key0": True, "key1": False}
print(dict_object["key0"])

__setitem__(self, key, value) — вызывается при присваивании какого-либо значения элементу в последовательности.
                                также может выбрасывать исключения TypeError и KeyError.
list_object = [1, 2, 3, 4, 5]
list_object[0] = 78
print(list_object)  #  [78, 2, 3, 4, 5]

dict_object = {"key0": True, "key1": False}
dict_object["key0"] = False
print(dict_object)  #  {"key0": False, "key1": False}

__delitem__(self, key) — вызывается при удалении значения в последовательности по его индексу (ключу) с помощью
                         синтаксиса ключевого слова del.
__missing__(self, key) — вызывается в случаях, когда значения в последовательности не существует.
__iter__(self) — вызывается методом iter(...) и возвращает итератор последовательности, например,
                 для использования объекта в цикле
__reversed__(self) — вызывается методом reversed(...) и аналогично методу __iter__ возвращает тот же итератор,
                     только в обратном порядке.
__contains__(self, item) — вызывается при проверке принадлежности элемента к последовательности с помощью in или not in.
"""


class Test:

    def __len__(self):
        print(10)
        return 10


test = Test()
print(len(test))


class Test:

    def __init__(self, seq):
        self.seq = seq

    def __getitem__(self, item):
        print('Method __getitem__ called')
        print(f'The item is {item}')
        return self.seq[item]


test = Test([1, 2, 3])
print(test[0])

test = Test("hello world")
print(test[0])

test = Test({'a': 'a', 'b': 2})
print(test['a'])
