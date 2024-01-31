import copy

#  Создание пустого множества
a = set()
print(a)

#  Создание множества из последовательности
a = set('Python')
print(a)

# Множества содержат только уникальные значения
a = set('Pythonn')
print(a)

#  Множество нельзя создать с помощью литерала {}
#  Но можно создать заполненное множество с его помощью
a = {'a', 'b', 'c'}
print(a)

#  генераторы множеств
a = {i*2 for i in range(5)}
print(a)

#  Операции, не изменяющие множества
#  len Число элементов в множестве (размер множества)
a = {1, 3, 5, 7, 8}
print(len(a))

#  in Проверяет принадлежность n множеству a. Если принадлежит, то возвращает True, иначе False.
a = {1, 3, 5, 7, 8}
print(3 in a)

#  == Проверяет равенство множеств
a = {1, 3, 4}
b = {3, 1, 4}
print(a == b)

#  Проверяет принадлежность элементов множества b множеству a.
#  Если а является подмножеством, то возвращает True, иначе False.
a = {1, 3, 4}
b = {3, 1}
print(b.issubset(a))

#  вместо issubset можно использовать >=
print(a >= b)

# union - объединение нескольких множеств
a = {1, 3, 4}
b = {3, 1, 5}
print(a.union(b))

#  вместо union можно использовать |
print(a | b)

#  intersection - Пересечение нескольких множеств
a = {1, 3, 4}
b = {3, 1, 5}
print(a.intersection(b))

#  вместо intersection можно использовать &
print(a & b)

# difference - Элементы множества а, не принадлежащие ни одному из множеств в скобках. Вычитание из множества а.
a = {1, 3}
b = {3, 1, 4, 5}
print(b.difference(a))

#  вместо difference можно использовать -
print(a - b)

#  symmetric_difference - Элементы, принадлежащие только одному из множеств a или b
a = {1, 3, 0}
b = {3, 1, 4, 5}
print(b.symmetric_difference(a))

#  вместо symmetric_difference можно использовать ^
print(b ^ a)

#  Создание копии множества.
a = {1, 3, 0}
b = a.copy()
print(b, end=' ')

#  вместо copy можно использовать =, но это создание еще одной ссылки на множество
c = a
print(c)

#  альтернатива
d = copy.deepcopy(a)



#  Операции, изменяющие множества

#  update - Объединение множеств, результат записывается в первое множество.
a = {1, 3, 0}
b = {2, 5}
a.update(b)
print(a)

#  вместо copy можно использовать |=
a = {1, 3, 0}
b = {2, 5}
a |= b
print(a)

#  intersection_update - Пересечение множеств, результат записывается в первое множество.
a = {1, 3, 2}
b = {2, 5}
a.intersection_update(b)
print(a)

#  вместо intersection_update можно использовать &=
a = {1, 3, 2}
b = {2, 5}
a &= b
print(a)

#  difference_update - Вычитание из множества множеств в скобках, результат записывается в первое множество.
a = {1, 3, 2}
b = {2, 5}
a.difference_update(b)
print(a)

#  вместо difference_update можно использовать -=
a -= b
print(a)

#  symmetric_difference_update - Элементы, принадлежащие только одному из множеств, a или b,
#  результат записывается в множество a.
a = {1, 3, 2}
b = {2, 5}
a.symmetric_difference_update(b)
print(a)

#  вместо symmetric_difference_update можно использовать ^=
a = {1, 3, 2}
b = {2, 5}
a ^= b
print(a)

# add - Добавляет элемент b в множество a.
a = {1, 3, 2}
a.add(5)
print(a)

#  remove - Удаляет элемент b из множества a. Если такого элемента нет, то ошибка: KeyError.
a = {1, 3, 2}
a.remove(3)
print(a)

try:
    a.remove(3)
except KeyError:
    pass

#  discard - Удаляет элемент b из множества a, не вызывая ошибку при отсутствии такого элемента.
a = {1, 3, 2}
a.discard(3)
a.discard(3)
print(a)

#  pop - Удаляет последний элемент из множества.
a = {4, 3, 2}
b = a.pop()
print(a)
print(b)

#  clear - Очищает множество от элементов.
a.clear()
print(a)

#  Перебор элементов множества
a = {1, 3, 2}
for i in a:
    print(i)

#  Неизменяемые множества
#  Неизменяемые множества frozenset представляют собой те же самые множества set,
#  за исключением того, что set – это изменяемый тип данных, а frozenset – неизменяемый тип данных.
#  Подобная ситуация была со списками и кортежами, где списки – изменяемый тип данных, а кортежи – неизменяемый.
a = set('Python')
b = frozenset('Pythonnn')

print(a == b)
print(type(a))
print(type(b))

#  генераторы множеств в Python - set comprehension
#  newSet = {expression for element in iterable}
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = {element*3 for element in l}
print(s)

s = {element for element in l if element % 2 == 0}
print(s)
