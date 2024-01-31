"""
синтаксис декоратора

@decorator
def F(arg):
    …

F(99) # Вызов функции


Это аналогично такому вызову функций

def F(arg):
    …

F = decorator(F)
F(99)

или
decorator(F)(99)


Сам декоратор является вызываемым объектом, возвращающим вызываемый объект.
То есть он возвращает объект, к которому производится обращение позже, когда декорированная функция
вызывается через свое исходное имя.


Общая кодовая схема, воплощающая идею декоратора:

def decorator(F):                 # При декорировании @
    def wrapper(*args):           # При вызове внутренней функции
        # Использование функции F и аргументов
        # F(*args) вызывает исходную функцию
    return wrapper


@decorator                        # func = decorator(func)
def func(x, y) :                  # func передается функции F декоратора
    …

func (6, 7)                       # 6, 7 передается аргументу ★args оболочки


Когда позже происходит обращение к имени func, в действительности вызывается функция wrapper, возвращенная
декоратором decorator; функция wrapper затем может запустить исходную функцию func, т.к. она по-прежнему доступна
в объемлющей области видимости. При реализации подобным образом каждая декорированная функция производит новую область
видимости для предохранения состояния.

"""


def simple_decorator(func):

    def inner():
        print('Начало работы декоратора...')
        func()
        print('Декоратор отработал!')

    return inner


@simple_decorator
def print_hi():
    print('Привет, я - функция, которую задекорировали!')

print_hi()


#  Декорирование функции с аргументами
def decorate_func_with_params(func):
    def inner(*args, **kwargs):
        print(f'Декорируем функцию с параметрами: {args}, {kwargs}')
        func(*args, **kwargs)
        print('Все прошло успешно!')
    return inner


@decorate_func_with_params
def adder(*nums):
    print(sum(nums))


print(adder(1))
print(adder(2, 7, 3))
print(adder(0, 33, 4, 10, 0))


#  Декораторы с параметрами
#  Аргументы декоратора используются, чтобы менять поведение самого декоратора
#  Для создания декоратора с параметрами добавляем еще один уровень вложенности
def repeater(attempts=1):
    def outer_decorator(func):
        def inner_decorator(*args, **kwargs):
            if attempts > 1:
                for _ in range(attempts):
                    print(func(*args, **kwargs))
            else:
                print(func(*args, **kwargs))

        return inner_decorator
    return outer_decorator


@repeater(3)
def print_msg(msg):
    return f'Message {msg}'


print_msg('MESSAGE!')
