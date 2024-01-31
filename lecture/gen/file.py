#  В отличие от нормальных функций, которые возвращают значение и прекращают работу,
#  генераторные функции автоматически приостанавливают и возобновляют свое выполнение
#  и состояние вокруг точки генерации значений.
#  По этой причине они служат альтернативой вычислению полной серии значений.
#  Состояние, которое генераторные функции сохраняют, когда приостанавливаются,
#  содержит местоположение в коде и полную локальную область видимости.

#  Генератор выдает значение, а не возвращает его —
#  оператор yield приостанавливает функцию и отправляет значение обратно вызывающему коду

#  Обычная функция
def func():
    return 1

#  Выполнилась и вернула результат
val = func()


#  Общий синтаксис генератора
def gen():
    ...
    yield ...
    ...


#  Общий синтаксис использования генератора
g = gen()
next(g)

#  когда исчерпали последовательность выбросили исключение
try:
    next(g)
except StopIteration:
    pass

#  так генератор наследует протокол итерации, то можно его использовать в цикле
for i in gen():
    pass


#  Объявляем функцию генератор, которая возводит в квадрат число
def square_all(numbers):
    for n in numbers:
        yield n**2


favorite_numbers = [6, 57, 4, 7, 68, 95]
squares = square_all(favorite_numbers)
#  в squares не сама функция и не результат ее, а объект генератора
print(type(squares))
for i in squares:
    print(i)


#  либо пишем так
squares = square_all(favorite_numbers)
print(next(squares))
print(next(squares))
print(next(squares))


#  Вместо функции генератора, можно использовать выражение генератора
#  работает идентично функции генератора
squares = (n**2 for n in favorite_numbers)
for i in squares:
    print(i)


#  Что использовать функцию генератора или выражение генератора?
#  выражение компактнее и лаконичнее, но не такое гибкое как функция
#  в выражение мы не можем добавить много логики и условий

squares = (n**2 for n in favorite_numbers)
#  В squares у нас так же генератор
print(type(squares))

next(squares)
next(squares)
next(squares)
next(squares)
next(squares)
#next(squares)
#next(squares)
#next(squares)


#  В функции генератора мы можем даже добавить return.
#  Он просто завершит выполнение генератора
def square_all(numbers):
    print('Inside function')
    for n in numbers:
        print('Inside for')
        yield n**2
        print('after yield')
        return 123

#  yield n**2 работает так же как return n**2, то есть возвращает текущее значение,
#  но не результат функции

#  Нет никакой разницы, что возвращать в return. Можно ничего не возвращать. return просто выход из функции

favorite_numbers = [6, 57, 4, 7, 68, 95]

print('================')

for i in square_all(favorite_numbers):
    print(i)


#  выражений yield может быть много в функции генератора
#  между вызовами yield можно добавлять любой код который будет выполняться


def gen1():
    for i in range(10):
        print(f"Block before first yield, item = {i}")
        yield i
        print(f"Block between yields, item = {i}")
        yield i
        print(f"Block after second yield, item = {i}")


g1 = gen1()
for i in g1:
    print(f'iteration, item = {i}')


#  yield может ничего не возвращать, точнее возвращать None

def gen2():
    for i in range(10):
        print(f"Block before first yield, item = {i}")
        yield
        print(f"Block between yields, item = {i}")
        yield
        print(f"Block after second yield, item = {i}")


g2 = gen2()
for i in g2:
    print(f'iteration, item = {i}')


#  У объекта генератора можно вызывать метод send
#  Он осуществляет переход на следующий элемент в серии результатов,
#  в точности как __next__, но также снабжает вызывающий код возможностью взаимодействия с генератором.
def gen():
    for i in range(10):
        print('inside for')
        x = yield i
        print('after yield')
        print(type(x))
        print(x)

g = gen()
print(next(g))
print(next(g))
g.send(10)
print(next(g))

#  Метод send можно применять, для написания генератора, который разрешает прекращать свою работу
#  за счет отправки кода завершения

#  Будем считать кодом завершения число 123
def gen():
    for i in range(10):
        x = yield i
        if x == 123:
            return '0101'
        print(x)

g = gen()
print(next(g))
print(next(g))
try:
    g.send(123)
except StopIteration:
    pass


#  send-ом можно передавать сколько угодно значений в генератор
def gen():
    for i in range(10):
        x = yield i
        y = yield
        if x == 123 and y == 123:
            return '0101'
        print(x)


g = gen()
print(next(g))
print(next(g))
g.send(123)
try:
    g.send(123)
except StopIteration:
    pass
