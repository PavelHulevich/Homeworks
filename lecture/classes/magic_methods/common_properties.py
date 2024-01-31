"""
Любой объект может содержать дополнительную информацию, полезную при отладке или приведении типов
__repr__(self) — информационная строка об объекте. Выводится при вызове функции repr(...) или в момент отладки.
                 Для последнего этот метод и предназначен. Например:
__str__(self) — вызывается при вызове функции str(...), возвращает строковый объект.
__bytes__(self) — аналогично __str__(self), только возвращается набор байт.
__format__(self, format_spec) — вызывается при вызове функции format(...) и используется для форматировании строки
                                с использованием строковых литералов.
"""


class Test:
    some_attr = 'some_attr'

    def __repr__(self):
        return f"I'm {self.__class__.__name__} class. I have {self.some_attr} attribute"


t = Test()
print(t)  # __repr__ вызывается когда принтим весь объект
print(repr(t))  # либо при вызове функции repr


class Test2:
    some_attr = 'some_attr'

    def __str__(self):
        return f"I'm {self.__class__.__name__} class. I have {self.some_attr} attribute"

test = Test2()
print(str(test))  # __str__ вызывается когда объект передаем функции str
