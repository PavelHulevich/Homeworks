import sys

print(sys.getsizeof(range(5)))
print(sys.getsizeof(range(500)))

res = range(5)
print(res)

type(zip([1, 2], [3, 4]))
print(sys.getsizeof(zip([1, 2], [3, 4])))
print(sys.getsizeof(range(5)))


res = map(lambda x: x * 2, [1, 2, 3, 4, 5])
print(res)
for i in res:
    print(i)

res = open('file.txt', 'r')
print(res)


#  контекстный менеджер with
with open('file.txt', 'r') as f:
    for line in f:
        print(line)


l = [1, 2, 3]


def check_prime(number):
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


#  класс итератора
#  класс реализует протокол итератора - методы __iter__ и __next__,
#  а также выбрасывает исключение StopIteration когда элементы закончились
class Primes:
    def __init__(self, max):
        self.max = max
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.number >= self.max:
            raise StopIteration
        elif check_prime(self.number):
            return self.number

        return self.__next__()


primes = Primes(20)
print(primes)

for x in primes:
    print(x)


#  функция-генератор
#  выражение yield возвращает значение, вычисленное на шаге итерации, но сохраняется состояние функции
#  на следующем шаге выполнение функции продолжается с того же места, где остановились.
#  Функция возвращает объект-генератор, который реализует протокол итератора.
def primes(max):
    number = 1
    while number < max:
        number += 1
        yield number


p = primes(20)
print(p)


for x in p:
    print(x)


#  функция-декоратор
#  декоратор добавляет к функции новое поведение, не изменяя ее код
#  декоратор первым аргументом принимает функцию, которую нужно декорировать
#  и возвращает функцию-обертку, которая будет вызываться до декорируемой функции
def lazy(fn):
    #  объявляем атрибут для объекта, в который будет добавлено значение, вычисленное в декорируемой функции
    attr_name = '_lazy'

    def _lazy_property(self):
        #  функции setattr/getattr добавляют/получают атрибут класса
        #  функция hasattr проверяет наличие атрибута класса по его имени
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return _lazy_property


class Country:
    def __init__(self, name, capital):
        self.name = name
        self.capital = capital

    @lazy
    def cities(self):
        print('cities method called')

        return ['city1', 'city2']


china = Country('China', 'Beijing')
print(china.cities())  # вызовется метод cities, значение будет сохранено в атрибуте _lazy
print(china.cities())  # метод cities уже не вызовется, значение будет получено из атрибута _lazy
print(china.cities())  # метод cities так же не вызовется, значение будет получено из атрибута _lazy


def match(lang):
    match lang:
        case 'Python' | 'Rust':
            print('Matched Python')
        case 'JAVA':
            print('Matched JAVA')
        case _:
            print('No Match')


print(match('Rust'))
print(match('JAVA2'))


def greeting(details):
    match details:
        case [time, name]:
            return f'Good {time} {name}!'
        case [time, *names]:
            msg = ''
            for name in names:
                msg += f'Good {time} {name}!\n'
            return msg


print(greeting(["Morning", "Ravi"]))
print(greeting(["Afternoon", "Guest"]))
print(greeting(["Evening", "Kajal", "Praveen", "Lata"]))


def intr(details):
    match details:
        case [amt, duration] if amt < 10000:
            return amt*10*duration/100
        case [amt, duration] if amt >= 10000:
            return amt*15*duration/100


print("Interest = ", intr([5000, 5]))
print("Interest = ", intr([15000, 3]))


n = 0
m = 2

#  вычислится только выражение до or, оно истинно. Вычисление выражения справа от or не произойдет.
if n == 0 or m % n == 0:
    print(1)


#  вызовет исключение на первом шаге, вычисление из-за этого не продолжится
#if m % n == 0 or n == 0:
#    print(1)


gre_score = 160
per_grad = 60

if gre_score > 10000:
    print(1)
else:
    if per_grad > 50:
        print(2)
    else:
        print(3)

