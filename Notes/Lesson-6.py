# #
# # функция Assert Инструкции assert в Python — это булевы выражения, которые проверяют, является ли
# # условие истинным (True). Они определяют факты (утверждения) в программе. Assertion — это проверка,
# # которую можно включить,
# # а затем выключить, завершив тестирование программы.
# # a = c = 1
# # b = 0
# # while a:
# #     # операторы
# #     pass  # - заполнитель. обозначает отсутсвие действий
# #     if a: break  # выход и цикла
# #     if c: continue  # переход в начало цикла
# #
# #     pass  # - заполнитель. обозначает отсутсвие действий
# #     ... # - липсис, тот же pass
# #
# # for 1:
# #     # операторы
# #     pass  # - заполнитель. обозначает отсутсвие действий
# #     if a: break  # выход и цикла
# #     if c: continue  # переход в начало цикла
# #
# #     pass  # - заполнитель. обозначает отсутсвие действий
# #     ... # - липсис, тот же pass
# #
# # кортежи
#
# T = (1, 2), (3, 4), (5, 6)
# for x in T:
#     a, b = x  # так тоже можно
#     a, _ = x  # если второй элемент не нужен
#     print(x)
#
# for (a, b) in T:
#     print(a, b)
#
# # словари
#
# D = {'a': 1, 'b': 2, 'c': 3}
# for key in D:
#     print(key, '==>', D[key])
#
# for (key, val) in D.items():
#     print(key, '==>', val)
#
# # вложенные циклы
# row = 5
# for i in range(0, row+1):
#     for j in range(i):
#         print('*', end='\t')  # табулятор в конце строки
#     print()
#
# for j in [1, 2]:
#     ...
#   #  break
# else:               # елсе в цикле сработает если не сработал брейк
#     print('Не попали в элсе из-за того что вызвали бреак')
# print('вообще вышли з цикла')
#
# sum = 0
# for i in range(2, 101, 2):
#     sum = sum + i
# print(i, sum)
#
# L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(len(L)):
#     L[i] += 1
#
# while i in L:
#     L[i] += 1
#     i += 1
#
# L1 = [1, 2, 3, 4]
# L2 = [5, 6, 7, 8]
# for (x, y) in zip(L1, L2):
#     print(x, y, '--', x + y)
#
#
# # разобраться
# # for (x, y) in map(lambda a, b: (a, b), L1, L2):
# #     print(x, y, '--', x + y)

# S = 'spam'
# for (index, item) in enumerate(S):
#     print(index, '---->', item)
#
# L = [1, 2]  # итерируемый объект
#
# # это типичный класс итератора
# class Iter:
#
#     def __next__(self):  # следующий объект из очереди
#         ...
#         raise StopIteration  # когда объекты кончились
#
#     def __iter__(self):  # смысл этого мэйджика - вернуть текущий объект итератора
#         return self
#
#
# iter1 = Iter  # в цикле первый вызов вызывает __iter__, потом в цикле уже зовет __next__
#
# f = open('file')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
#
L = [1, 2, 3]
I = iter(L)
# I.__next__()
# I.__next__()
# I.__next__()

while True:
    try:
        x = next(I)
    except StopIteration:
        break
    print(x ** 2, end=' ')

    в задании 6: 0 - завершает ввод массива
    7 - принимаем список чисел
    10 - лучше со стеком делать