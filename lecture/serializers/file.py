#  Сериализация - процесс преобразования информации из одного вида в другой, из одного типа в другой.
#  Десериализация - процесс обратный сериализации, восстановление данных в исходных типах.


#  Pickle является встроенным методом сериализации объекта.
#  Интерфейс pickle обеспечивает четыре метода:
#       dump сериализует в открытый файл,
#       dumps сериализует в строку,
#       load десериализует из открытого файлового объекта,
#       loads десериализует из строки


from datetime import datetime

simple = dict(
    int_list=[1, 2, 3],
    text='string',
    number=3.44,
    boolean=True,
    none=None,
)


class A:

    def __init__(self, simple):
        self.simple = simple

    def __eq__(self, other):
        if not hasattr(other, 'simple'):
            return False
        return self.simple == other.simple

    def __ne__(self, other):
        if not hasattr(other, 'simple'):
            return True
        return self.simple != other.simple


a = A(simple=simple)

complex = {
    'a': a,
    'when': datetime(2016, 3, 7),
}


import pickle

"""
pickle.dump()
pickle.dumps()

pickle.load()
pickle.loads()
"""

#  Pickle поддерживает двоичный протокол, результат этих операций бинарный тип
print(pickle.dumps(simple, protocol=0))
print(pickle.dumps(simple, protocol=1))
print(pickle.dumps(simple, protocol=pickle.DEFAULT_PROTOCOL))
print(pickle.dumps(simple, protocol=pickle.HIGHEST_PROTOCOL))

#  По умолчанию передавать протокол не обязательно,
#  делается это для обратной совместимости с разными версиями языка и библиотеки pickle
#  достаточно такого вызова
print(pickle.dumps(simple))


#  dumps сериализует в файл, открытый в бинарном режиме записи wb - write binary
pickle.dump(simple, open('simple0.pkl', 'wb'), protocol=0)
pickle.dump(simple, open('simple1.pkl', 'wb'), protocol=1)
pickle.dump(simple, open('simple2.pkl', 'wb'), protocol=pickle.HIGHEST_PROTOCOL)

#  loads десериализует из строки, а не из файла
x = pickle.loads(b'\x80\x04\x95O\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x08int_list\x94]\x94(K\x01K\x02K\x03e\x8c\x04text\x94\x8c\x06string\x94\x8c\x06number\x94G@\x0b\x85\x1e\xb8Q\xeb\x85\x8c\x07boolean\x94\x88\x8c\x04none\x94Nu.')

#  проверяем, что после десериализации объект восстаносилися и полностью соответствует объекту, до сериализации
assert x == simple


#  пробуем сериализовать сложный объект, состоящий из нашего класса и объекта datetime
print(pickle.dumps(complex))
print(pickle.dumps(complex, protocol=pickle.HIGHEST_PROTOCOL))


#  пробуем сериализовать сложный объект в файл
pickle.dump(complex, open('complex1.pkl', 'wb'))
pickle.dump(complex, open('complex5.pkl', 'wb'), protocol=pickle.HIGHEST_PROTOCOL)


#  JSON (JavaScript Object Notation) является частью стандартной библиотеки Python.
#  Сериализует объекты в текстовый формат
#  Интерфейс json обеспечивает четыре метода:
#       dump сериализует в открытый файл,
#       dumps сериализует в строку,
#       load десериализует из открытого файлового объекта,
#       loads десериализует из строки
import json

print(type(json.dumps(simple)))
print(json.dumps(simple))
#  Результат выглядит довольно читаемым, но нет отступовб добавим отступы:
print(json.dumps(simple, indent=4))


#  десериализуем объект из строки назад в объект
x = json.loads(json.dumps(simple))
assert x == simple

#  json сам умеет преобразовывать объекты простых типов - строки, списки, числа, булевы, None, дикты.
#  но он не знает как преобразовывать сложные объекты - классы, написанные программистами, datetime и тд
try:
    json.dumps(complex)
except TypeError:
    pass


#  чтобы json мог сериализовать сложные объекты, мы должны добавить к сериализатору простых типов, логику,
#  для сериализации наших, сложных объектов.
#  Формат, во что будет преобразован наш объект, этому кастомному сериализатору не важен.
#  Лишь бы объекты были простых типов.
#  Выходной формат важен только второй стороне, которая будет получать эти данные и
#  преобразовывать в объекты, с которыми она будет работать.
#  О формате надо договориться заранее, и не менять его просто так.
class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return {'__datetime__': o.replace(microsecond=0).isoformat()}
        elif isinstance(o, A):
            return {'__{}__'.format(o.__class__.__name__): o.__dict__}

        return o

#  строчки ниже всего лишь протокол (договоренность) с другой стороной, что эти объекты должны быть преобразованы так
#  return {'__datetime__': o.replace(microsecond=0).isoformat()}
#  return {'__{}__'.format(o.__class__.__name__): o.__dict__}
#  можно делать и по другому
#  return o.replace(microsecond=0).isoformat()
#  return [(k, v) for k, v in o.__dict__.items()]

complex = {
    'a': a,
    'when': datetime(2016, 3, 7),
    'arg': 1,
}
#  передаем свой кастомный сериалайзер CustomEncoder в момент сериализации
serialized = json.dumps(complex, indent=4, cls=CustomEncoder)


print(serialized)

#  десериализация завершилась успешно, но мы не восстановили некоторые объекты до их изначально состояния
deserialized = json.loads(serialized)
print(deserialized == complex)
#  json ничего не знает о них


def decode_object(o):
    if '__A__' in o:
        return A(o['__A__'])
    elif '__datetime__' in o:
        return datetime.strptime(o['__datetime__'], '%Y-%m-%dT%H:%M:%S')
    return o

#  значит нам нужен свой собственный десериализатор, который следуя, контракту, согласованному для сериализации
#  восстановит объекты до их исходных состояний
deserialized = json.loads(serialized, object_hook=decode_object)
print(deserialized)
