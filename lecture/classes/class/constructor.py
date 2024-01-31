"""
В Python разделяют конструктор класса и метод для инициализации экземпляра класса.

Конструктор класса это метод __new__(cls, *args, **kwargs) для инициализации экземпляра класса используется метод
__init__(self). При этом, как вы могли заметить __new__ – это классовый метод, а __init__ таким не является.
Метод __new__ редко переопределяется, чаще используется реализация от базового класса object, __init__ же наоборот
является очень удобным способом задать параметры объекта при его создании.
"""


class MyClass:

    def __new__(cls, *args, **kwargs):
        return

    def __init__(self):
        pass


class Rectangle(object):

    def __new__(cls, *args, **kwargs):
        print("Hello from __new__")
        return super().__new__(cls)

    def __init__(self, width, height):
        print("Hello from __init__")
        self.width = width
        self.height = height


rect = Rectangle(10, 20)

print(rect.width)
print(rect.height)


# пример использования конструктора класса

## разрабатываем класс для работы с БД. В частности, через него можно будет подключаться к СУБД,
## читать и записывать информацию, закрывать соединение:

class DataBase:

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("закрытие соединения с БД")

    def read(self):
        return "данные из БД"

    def write(self, data):
        print(f"запись в БД {data}")


## И далее полагаем, что в программе должен существовать только один экземпляр этого класса в каждый момент ее работы.
## То есть, одновременно два объекта класса DataBase быть не должно. Чтобы это обеспечить и гарантировать, как раз и
# используется паттерн Singleton. Реализуем его для класса DataBase.

class DataBase:

    #  атрибут для хранения ссылки на экземпляр этого класса. Если экземпляра нет,
    #  то атрибут будет принимать значение None.
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self, user, passwd, port):
        self.user = user
        self.passwd = passwd
        self.port = port

    def connect(self):
        print(f"соединение с БД: {self.user}, {self.passwd}, {self.port}")


db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)

print(id(db), id(db2))  # id ожидаемо равны, ссылки db и db2 действительно ведут на один объект.

db.connect()
db2.connect()
#  при повторном вызове DataBase() также был вызван магический метод __init__ с новым набором аргументов
#  и локальные свойства изменили свое значение.
