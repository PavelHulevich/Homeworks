import copy

#  Создание пустого словаря
a = {}
print(a)

a = dict()
print(a)

#  Динамическое создание словаря
a = {}
a['name'] = 'Kate'
a['age'] = 20
print(a)

#  Словарь с заданными ключами и значениями:
d = {1: 'Kate', 'age': 20}
print(d)

#  При создании словаря С помощью функции dict ключи обязательно должны быть строками.
#  Причем ключ не заключаем в кавычки. Данный способ позволяет создать словарь из пар значений.
a = dict(name='Kate', age=20, сity='Minsk')
print(a)

#  SyntaxError:
#  a = dict(1='Kate', age=20, сity='Minsk')


#  Также словарь можно быстро создать из двух последовательностей используя функцию zip()
a = ['name', 'age', 'city']
b = ['Kate', 20, 'Minsk']
c = dict(zip(a, b))
print(c)


#  fromkeys. Создает словарь по списку ключей с пустыми значениями.
a = {}.fromkeys(['name', 'age'])
print(a)

#  Также можно после запятой указать значение по умолчанию для всех полей.
#  Однако таким способом нельзя указать разные значения по умолчанию для каждого ключа.
a = {}.fromkeys(['name', 'age'], 20)
print(a)

a = {}.fromkeys(['name', 'age'], ['Kate', 20])
print(a)

#  С помощью генератора
a = {i: i**2 for i in range(3)}
print(a)

#  Ввод с клавиатуры
#  a = {input('Введите ключ: '):input('Введите значение: ') for i in range(2)}
#  print(a)

#  Получение данных из словаря по ключу
a = {'name': 'Kate', 'age': 20}
print(a['name'])

#  При попытке получить значение из словаря по несуществующему ключу получим ошибку.
a = {'name': 'Kate', 'age': 20}
try:
    print(a['city'])
except KeyError:
    pass

#  Обновление данных в словаре
a = {'name': 'Kate', 'age': 20}
a['name'] = 'Nick'
print(a)

#  А если напишем следующим образом то, поскольку ключа 'city' в словаре нет, добавится новое значение
a = {'name': 'Kate', 'age': 20}
a['city'] = 'Minsk'
print(a)

#  Удаление элементов словаря
a = {'name': 'Kate', 'age': 20, 'city': 'Minsk'}
del a['name']
print(a)

#  Если во время удаления указать несуществующий ключ, то получим ошибку
a = {'name': 'Kate', 'age': 20, 'city': 'Minsk'}
del a['name']
try:
    del a['name']
except KeyError:
    pass

#  Очистка словаря
a.clear()
print(a)

#  Удаление всего словаря
a = {'name': 'Kate', 'age': 20}
del a
#print(a)  NameError


#  Основные функции и методы словаря
a = {'name': 'Kate', 'age': 20, 'city': 'Minsk'}

#  len() возвращает количество записей в словаре
print(len(a))

#  clear() очищает словарь
a.clear()
print(a)

#  copy() создает копию словаря
a = {'name': 'Kate', 'age': 20, 'city': 'Minsk'}
b = a.copy()
print(b)

#  альтернатива
d = copy.deepcopy(b)
print(d)

#  при изменении оригинального cловаря, словари, созданные с помощью .copy() и copy.deepcopy() не меняются
print(a)
print(b)
print(d)

a['name'] = 'Nick'
print(a)
print(b)
print(d)

#  get(key, default)  возвращает значение по ключу.
#  Если такого ключа нет, то возвращает значение, указанное в параметре default.
#  По умолчанию оно равно None
print(a.get('name'))
print(a.get('name1'))
print(a.get('name1', 'Ключ не найден'))

#  возвращает все пары ключ: значение
print(a.items())

#  возвращает ключи в словаре
print(a.keys())

#  возвращает все значения в словаре
print(a.values())


#  pop(key[, default]) – удаляет ключ key из словаря и возвращает значение.
#  Если ключ отсутствует в словаре, возвращает значение, указанное в default,
#  а если default не указан, то вызывает исключение
age = a.pop('age')
print(a)
print(age)

print(a.pop('age1', 'Элемент отсутствует'))
age1 = a.pop('age1', 0)
print(age1)

try:
    print(a.pop('age1'))
except KeyError:
    pass

#  popitem() – удаляет из словаря и возвращает последнюю пару ключ:значение.
#  Если словарь не содержит элементов, то возвращает исключение.
a = {'name': 'Kate', 'age': 20, 'city': 'Minsk'}
b = a.popitem()
print(b)
print(a)

b = a.popitem()
print(b)
print(a)

b = a.popitem()
print(b)
print(a)

try:
    b = a.popitem()
except KeyError:
    pass

print(a)


#  Перебор элементов словаря при помощи цикла
a = {'name': 'Kate', 'age': 20, 'city': 'Minsk'}
#  keys() возвращающий список всех ключей словаря
for i in a.keys():
    print(i, '-', a[i])

#  альтернатива
a = dict(name='Kate', age=20, сity='Minsk')
for i in a:
    print(i, '-', a[i])


#  values() возвращающий список всех значений словаря
for i in a.values():
    print(i)


#  items() возвращающий кортеж ключей и значений словаря
for k, v in a.items():
    print(k, '-', v)


#  Генераторы словарей - dict comprehension
#  dict_variable = {key:value for (key,value) in dictonary.items()}

#  метод преобразования одного словаря в другой
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict2 = {key: value for (key, value) in dict1.items()}
print(dict2)

#  метод создания нового словаря
dict2 = {str(i): i for i in [1, 2, 3, 4]}
print(dict2)

dict2 = {str(i): j for i, j in [(1, 2), (3, 4)]}
print(dict2)

#  делаем составной ключ - кортеж, полезно когда захотим уменьшить количество вложенных итераций по многомерному словарю
dict2 = {(i, j): k for i, j, k in [(1, 2, ['a', 'b', 'c']), (3, 4, ['a', 'b', 'c'])]}
print(dict2)

#  нельзя делать изменяемы тип данных ключем
#  Python не может построить хэш для изменяемого типа данных
#  dict2 = {k: (i, j) for i, j, k in [(1, 2, ['a', 'b', 'c']), (3, 4, ['a', 'b', 'c'])]}  TypeError


#  можем поменять значение элемента словаря
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict2 = {key: value+1 for (key, value) in dict1.items()}
print(dict2)

#  можем поменять ключ элемента словаря
dict2 = {key+'a': value for (key, value) in dict1.items()}
print(dict2)

#  можем поменять ключ и значение элемента словаря
dict2 = {key+'a': value+1 for (key, value) in dict1.items()}
print(dict2)

#  чуть сложнее, преобразовываем температуру в фаренгейтах в цельсии
fahrenheit = {'t1': -30, 't2': -20, 't3': -10, 't4': 0}
celsius = {k: (float(5)/9)*(v-32) for (k, v) in fahrenheit.items()}
print(celsius)


#  Условие if
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#  Предположим, вам нужно создать новый словарь из имеющегося, но с элементами, большими 2
dict2 = {k: v for (k, v) in dict1.items() if v > 2}
print(dict2)

#  Допустим, что нам нужно не только получить элементы, большие двух, но и одновременно проверить, кратны ли они двум
dict3 = {k: v for (k, v) in dict1.items() if v > 2 and v % 2 == 0}
print(dict3)

#  То же самое, но 2 условия подряд
dict4 = {k: v for (k, v) in dict1.items() if v > 2 if v % 2 == 0}
print(dict4)


#  Вложенные генераторы словарей
#  пишем сначала генератор для обхода внешнего словаря:
#  {outer_k: outer_v for (outer_k, outer_v) in outer_dictionary.items()}
#  теперь вместо outer_v записываем генератор для обработки внутреннего словаря:
#  {outer_k: {inner_k: inner_v for (inner_k, inner_v) in outer_v.items()} for (outer_k, outer_v) in nested_dict.items()}

nested_dict = {'first': {'a': 1}, 'second': {'b': 2}}
float_dict = {outer_k: {float(inner_v) for (inner_k, inner_v) in outer_v.items()} for (outer_k, outer_v) in nested_dict.items()}
print(float_dict)

#  другой способ
float_dict = {}
for outer_k, outer_v in nested_dict.items():
    for inner_k, inner_v in outer_v.items():
        float_dict[inner_k] = inner_v
print(float_dict)

