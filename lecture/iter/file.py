L = [1, 2]  # Итерируемый объект


print('Протокол итерации: __next__ - для следующего элемента, __iter__ - вернуть итератор и выбросить исключение StopIteration когда исчерпали последовательность')


class Iter:

    def __next__(self):
        ...
        raise StopIteration

    def __iter__(self):
        return self


iter1 = Iter()


print('Протокол итерации работает для файлов, через меджик метод')
f = open('file')
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())

print('Протокол итерации работает для файлов, через меджик метод')
f = open('file')
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
#print(f.__next__())
#print(f.__next__())

print('Протокол итерации работает для файлов, не обязательно использовать меджик метод, можно и встроенную функцию next - предпочтительнее')
f = open('file')
next(f)
next(f)
next(f)
next(f)
#next(f)
#next(f)
#next(f)
#next(f)



print('Протокол итерации работает для списков, так же как и для других итерируемых объектов')
L = [1, 2, 3]
I = iter(L)
I.__next__()
I.__next__()
I.__next__()
#I.__next__()


# автоматическая итерация
L = [1, 2, 3]
for X in L:
    print(X ** 2, end=' ')


# ручная итерация
I = iter(L)
while True:
    try:
        X = next(I)
    except StopIteration:
        break

    print(X ** 2, end=' ')
