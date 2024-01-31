"""
Любое описание объекта в объектно-ориентированном программировании начинается с создания объекта и его удаления.
__new__(cls[, ...]) — метод создания типа класса. Он принимает первым аргументом тип класса, в котором он вызывается,
                      и возвращает этот же тип. В основном используется, чтобы настраивать создание экземпляра класса
                      тех объектов, которые наследуются от неизменяемых типов (например, int, str, или tuple).
__init__(self[, ...]) — инициализатор класса. Используется при определении объектов.
__init_subclass__(cls) — позволяет переопределить создание подклассов объекта.
__del__(self) — деструктор класса. Вызывается автоматически сборщиком мусора, практически никогда не используется,
                за исключением, когда пользователя необходимо предупредить о незакрытых дескрипторах.
"""

#  добавление дополнительного атрибута


class Test:

    def __init_subclass__(cls, test_param, **kwargs):
        print("Method __init_subclass__ called")
        print(cls, type(cls))
        print(test_param, type(test_param))
        print(kwargs, type(kwargs))

        super().__init_subclass__(**kwargs)  #  вызов метода родительского класса, от которого наследуется каждый класс
        cls.test_param = test_param


class AnotherTest(Test, test_param="Hello World"):
    pass


t = Test()
try:
    print(t.test_param)
except AttributeError:
    print('__init_subclass__ not called for parent class')

#  __init_subclass__ вызывается только для классов-потомков
at = AnotherTest()
print(at.test_param)
