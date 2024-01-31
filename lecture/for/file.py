"""
for цель in объект:                   # Присваивает цели элементы объекта
    цель += 1
    операторы
    if проверка: break                # Выход из цикла с пропуском else
    if проверка: continue             # Переход в начало цикла
else:
    операторы                         # Если не встречался оператор break
"""


#  For и строки
str = "Python"
for i in str:
    print(i)


#  For и список
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 5
for i in L:
    c = n*i
    i += 2  #  Можем менять переменную (цель), и использовать внутри цикла, но на следующем шаге итерации она перезатрется новым элементом списка
    print(c)

print(i)  #  после выхода из цикла переменная (цель) все еще доступна и содержит значение последнего элемента цикла или измененное значение, если меняли


#  For и список кортежей
T = [(1, 2), (3, 4), (5, 6)]
for x in T:
    print(x)

for x in T:
    a, _ = x  #  распаковываем кортеж по переменным внутри цикла
    print(a)

for (a, b) in T:  #  распаковываем кортеж по переменным на шаге итерации цикла
    print(a, b)

for a, b in T:  #  Круглые скобки не обязательны
    print(a, b)


#  For и словарь, по умолчанию работает с ключами
D = {'а': 1, 'b': 2, 'c': 3}
for key in D:
    print(key, '=>', D[key])

#  С помощью встроеного метода items можно распаковать элемент словаря в ключ и значение
for (key, value) in D.items():
    print(key, '=>', value)


#  Круглые скобки не обязательны
for key, value in D.items():
    print(key, '=>', value)


"""
Вложенные циклы:

for iterating_var1 in sequence:  #outer loop  
    for iterating_var2 in sequence:  #inner loop  
        #block of statements     

#Other statements

"""

rows = 5
for i in range(0, rows+1):
    for j in range(i):
        print("*", end='\t')

    print()


items = [111, (4, 5)]
tests = [(4, 5), 3.14]
for key in tests:
    for item in items:
        if item == key:
            print(key, 'was found')
            break
    else:
        print(key, "not found!")


for j in [1, 2]:
    if 1:
        flag = 0
        break
    else:
        flag = 1
else:
    print('Не попали в else из-за того что вызвали break')

print('Вообще вышли из цикла')


flag = 0
for j in [1, 2]:
    ...
else:
    flag = 1
    print('Попали в else из-за того что не вызвали break')

flag = 1


if flag:
    ...
else:
    ...


items = [111, (4, 5)]
tests = [(4, 5), 3.14]
for key in tests:
    for item in items:
        if item == key:
            print(key, 'was found')
            break
    else:
        print(key, "not found!")


#  Упростили циклы выше, убрали вложенный цикл
for key in tests:
    if key in items:
        print(key, 'was found')
    else:
        print(key, "not found!")


#  continue - вернулись в начало
i = 0
for i in range(10):
    i += 1
    if i == 5:
        continue
    print(i)


str = "Python"
for i in str:
    if i == 't':
        continue
    print(i)

# range(start, stop, step size)
range(1, 5)


#  Цикл for и range
S = 'spam'
for i in range(len(S)):
    S = S[i:] + S[:i]
    print(S, end=' ')


#  Работает и со списками
L = [1, 2, 3]
for i in range(len(L)):
    X = L[i:]+L[:i]
    print(X, end=' ')
print('')

S = 'abcdefghijk'
print(list(range(0, len(S), 2)))
for i in range(0, len(S), 2):
    print(S[i], end=' ')

#  Предыдущий цикл можно сделать проще через срез
S = 'abcdefghijk'
for c in S[::2]:
    print(c, end=' ')

print('')
#  Поменяли значение в цикле
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(L)):
    L[i] += 1

print(L)


print('')

#  Параллельная обработка нескольких последовательностей с помощью zip в одном цикле
L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
for (x, y) in zip(L1, L2):
    print(x, y, '--', x + y)


#  Тоже самое но с lambda
for (x, y) in map(lambda a, b: [a, b], L1, L2):
    print(x, y, '--', x + y)


#  Обращаемся к элементу последовательности по индексу
S = 'spam'
offset = 0
for item in S:
    print(S[offset], 'appears at offset', offset)
    offset += 1


#  Тоже самое, но без использования дополнительных переменных
for (offset, item) in enumerate(S):
    print(item, 'appears at offset', offset)
