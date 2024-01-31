"""
класс является объектом, а потому:
    • его можно присвоить переменной,
    • его можно скопировать,
    • можно добавить к нему атрибут,
    • его можно передать функции в качестве аргумента,
"""

#  Например, можно создать класс в функции, используя ключевое слово class:


def choose_class(name):
    if name == 'foo':
        class Foo:
            pass
        return Foo  # возвращает класс, а не объект
    else:
        class Bar:
            pass
        return Bar


MyClass = choose_class('foo')
print(MyClass)
print(MyClass())

MyClass.asd = 123
print(MyClass().asd)

print("================================================")
#  С помощью функции type можно создавать классы на ходу. Type принимает на вход описание класса и возвращает класс.
MyClass = type('MyClass', (), {})
print(MyClass)
print(MyClass())  # создаёт экземпляр класса

print("================================================")

#  type принимает словарь, определяющий атрибуты класса:


class Foo:
    bar = True


#  можно переписать как
Foo = type('Foo', (), {'bar': True})
print(Foo)
print(Foo())  # создаёт экземпляр класса


print("================================================")

def print_bar(self):
    print(self.bar)

#  Добавим методы классу, а так же наследуем его от другого класса.

FooChild = type('FooChild', (Foo,), {'print_bar': print_bar})
print(FooChild)
print(FooChild())  # создаёт экземпляр класса
FooChild().print_bar()


#  В Питоне классы являются объектами и можно создавать классы на ходу.
#  Это именно то, что Питон делает, когда используется ключевое слово class, и делает он это с помощью метаклассов.
#  Метакласс это «штука», которая создаёт классы. Они полезны для сложных вещей. Но сами по себе они просты:
#     • перехватить создание класса
#     • изменить класс
#     • вернуть модифицированный


class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        print("__call__")
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]


class DataBase(metaclass=SingletonMeta):

    def __init__(self, user, password, port):
        print("__init__")
        self.user = user
        self.password = password
        self.port = port

    def connect(self):
        print(f"соединение с БД: {self.user}, {self.password}, {self.port}")


db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)

print(id(db), id(db2))
db.connect()
db2.connect()
