
class Immutable:

    def __new__(cls, v):
        cls.v = v
        obj = super().__new__()
        return obj

    def __setattr__(self, key, value):
        ...

    def __delattr__(self, item):
        ...


i = Immutable(5)
i.asd = 123

print(i)
