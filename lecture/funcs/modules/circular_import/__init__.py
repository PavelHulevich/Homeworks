"""
Циклический импорт в Python – это форма циклической зависимости, которая создается с помощью оператора импорта в Python.

# module1
import module2
module2.function2()
def function3():
    print('Goodbye, World!')



# module2
import module1
def function2():
    print('Hello, World!')
    module1.function3()


# __init__.py
import module1


Циклический импорт – это результат плохого дизайна. Зависимые функции могут быть перемещены в другие модули,
которые не будут содержать циклическую ссылку. Иногда оба модуля можно просто объединить в один более крупный.

# module 1 2

def function1():
    function2()

def function2():
    print('Hello, World!')
    function3()

def function3():
    print('Goodbye, World!')

function1()


Однако объединенный модуль может иметь некоторые несвязанные функции (тесная связь) и может стать очень большим,
если в двух модулях уже есть много кода. Так что, если это не сработает, можно было бы отложить импорт module2,
чтобы импортировать его только тогда, когда это необходимо. Это можно сделать, поместив импорт module2 в
определение function1():
# module 1

def function1():
    import module2
    module2.function2()

def function3():
    print('Goodbye, World!')

# __init__.py
import module1

"""


import module1