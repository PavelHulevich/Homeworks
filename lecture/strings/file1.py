# Сложение (конкатенация)
s1 = 'Hello'
s2 = 'world'
s3 = s1 + s2
print(s3)


#  Вычитание
s1 = 'Hello world'
s2 = 'world'
s3 = s1.replace(s2, '')
print(s3)


#  Дублирование (умножение)
st = 'ab ' * 6
print(st)


#  Принадлежность строки
s1 = 'Иван Иванов'
s2 = 'Иван'

if s2 in s1:  # Проверяем, есть ли «содержимое» строки s2 в s1
    print('Пользователь Иван есть в нашей базе данных')
else:
    print('Пользователь Иван в базе данных отсутствует')


#  Определение длины строки
ln = len('Hello World')
print(ln)
s1 = 'Hello'
print(len(s1))


#  Доступ по индексу
st = 'HelloWorld'
print(st[0])
print(st[1])
print(st[2])

st = 'HelloWorld'
#  print(st[20])  # IndexError: string index out of range
#  print(st[-11])  # IndexError: string index out of range


#  Срез строки
st = 'HelloWorld'
print(st[0:3])
print(st[2:5])
print(st[4:7])


st = 'HelloWorld'
print(st[:6])  # Срез с начала строки
print(st[5:])  # Срез до конца строки
print(st[:])  # Целая строка


st = 'HelloWorld'
print(st[-7:-4])  # Срез с отрицательными индексами
print(st[-4:-4])  # Начальный индекс равен конечному
print(st[-4:])  # Срез до конца строки
print(st[:-3])  # Срез с начала строки
print(st[-7:4])  # Срез с положительным и отрицательным индексами


#  Шаг извлечения среза
st = 'Helloworld'
print(st[6:1:-2])


#  Методы поиска подстроки
s = 'HelloworldHelloworld '
sub = 'wor'

print(s.find(sub))  # Возвращает индекс первого совпавшего значения подстроки
print(s.rfind(sub))  # Возвращает индекс последнего совпавшего значения подстроки

s = 'HelloworldHelloworld'
print(s.rfind('abc'))  # Если подстроки в строке нет, Python возвращает −1


#  Методы преобразования символов строки в верхний и нижний регистры
S = 'Helloworld 23'

print(S.upper())  # Переводит все символы в верхний регистр
print(S.lower())  # Переводит все символы в нижний регистр
print(S)  # Проверяем значение исходной строки


#  Метод разбиения строки по разделителю
S = 'Cat, Dog,Hamster   Rabbit, Pig'

print(S.split())  # Разделитель не задан. Метод разбивает строку по пробельным символам — пробелу и знаку табуляции
print(S.split(','))  # Разбивает строку по заданному разделителю ','
print(S.split(',', 2))  # Задаёт максимальное количество разбиений


S = 'Hi!'
print(S.rjust(10, '*'))  # Увеличивает длину строки до 10 и заполняет пробелы слева символами '*'
print(S.ljust(10, '*'))  # Увеличивает длину строки до 10 и заполняет пробелы справа символами '*'


myTuple = ('John', 'Peter', 'Vicky')
x = '#'.join(myTuple)
print(x)

myDict = {'name': 'John', 'country': 'Norway'}
mySeparator = 'TEST'
x = mySeparator.join(myDict)
print(x)


print('Hello'.replace('l', 'L'))
print('Abrakadabra'.replace('a', 'A', 2))


#  Метод count
print('Abracadabra'.count('a'))  # 4
print(('a' * 10).count('aa'))  # 5


#  Форматирование
# f-strings
python_version = 3.11
print(f'python_version={python_version}')
print(f'{python_version=}')


#  Выравнивание справа
number = 20
print(f'number={number}')
print(f'{number:8}')
print(f'{number:>8}')
print(f'{number:_>8}')


#  Выравнивание слева
print(f'{number:<8}')
print(f'{number:_<8}')


#  Выравнивание по центру
print(f'{number:^8}')
print(f'{number:*^8}')


#  Форматирование даты
import datetime
now = datetime.datetime.now()
print(f'Today is {now:%B} {now:%-d}, {now:%Y}')
print(f'{now=:%m-%d-%Y}')


#  Разделитель тысяч
x = 1000000
print(f'{x:,}')

num = 2343552.6516251625
print(f'{num:,.3f}')


#  Форматирование числа в экспоненциальном представлении.
num = 2343552.6516251625
print(f'{num:e}')
print(f'{num:E}')
print(f'{num:.2e}')
print(f'{num:.4E}')


# ''.format()
'Hello, my name is {}. I am a {} turned {}.'.format('Jessica', 'musician', 'programmer')


#  Позиционные аргументы
print('Steve plays {0} and {1}.'.format('trumpet', 'drums'))
print('Steve plays {1} and {0}.'.format('trumpet', 'drums'))


'Hello, my name is {name}. I am a {profession1} turned {profession2}.'.format(name='Jessica', profession1='musician', profession2='programmer')


#  Именованные аргументы
print('{organization} is {adjective}!'.format(organization='Python', adjective='awesome'))
print('{adjective} is {organization}!'.format(organization='Python', adjective='awesome'))


#  Именованные и позиционные аргументы
name = 'Sam'
adjective = 'amazing'
number = 200
disney_ride = 'Space Mountain'
s = 'I went to {0} with {name}.\nIt was {adjective}.\nWe waited for {hours} hours to ride {ride}.'
print(s.format('Disneyland', name=name, adjective=adjective, hours=number, ride=disney_ride))


# ключи, атрибуты и смещения
import sys

print('Му {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'}))
print('My {map[kind]} runs {sys.platform}'.format(sys=sys, map={'kind': 'laptop'}))

somelist = list('SPAM')
print(somelist)
s = 'first={0[0]}, third={0[2]}'.format(somelist)
print(s)
s2 = 'first={0}, last={1}'.format(somelist[0], somelist[-1])
print(s2)
parts = somelist[0], somelist[-1], somelist[1:3]
s3 = 'first={0}, last={1}, middle={2}'.format(*parts)
print(s3)


#  Выравнивание
print('{0:10} = {1:10}'.format('spam', 123.4567))
print('{0:>10} = {1:<10}'.format('spam', 123.4567))
print('{:*^30}'.format('centered'))
print('{0.platform:>10} - {1[kind]:<10}'.format(sys, dict(kind='laptop')))


#  Номер аргумента можно опускать
print('{:10} = {: 10}'.format('spam', 123.4567))
print('{:>10} = {:<10}'.format('spam', 123.4567))
print('{.platform:>10} = {[kind]:<10}'.format(sys, dict(kind='laptop')))


#  Округление чисел с плавающей точкой
print('{0:f}, {1:.2f}, {2:06.2f}'.format(3.14159, 3.14159, 3.14159))


#  Шестнадцатеричный, восьмеричный и двоичный форматы
print('{0:x}, {1:o}, {2:b}'.format(255, 255, 255))
print('int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}'.format(42))


#  Параметры форматирования можно динамически получать из списка аргументов
print('{0:.2f}'.format(1 / 3.0))
print('{0:.{1}f}'.format(1 / 3.0, 4))  # Получение значений из аргументов


#  %
s = 'This is a string %s' % 'string value goes here'
print(s)
print('Hi, my name is %s' % 'Sam')

print('%s=%s' % ('spam', 42))
print('%s, %s and %s' % (3.14, 42, [1, 2]))


#  Именованные аргументы
print('My %(kind)s runs %(platform)s' % {'kind': 'laptop', 'platform': sys.platform})

'Hello, my name is %(name)s. I am a %(profession1)s turned %(profession2)s.' % {'name': 'Jessica', 'profession1': 'musician', 'profession2': 'programmer'}


#  Форматирование списков
somelist = list('SPAM')
parts = somelist[0], somelist[-1], somelist[1:3]
print('first=%s, last=%s, middle=%s' % parts)


#  Выравнивание
print('%-10s = %10s' % ('spam', 123.4567))
print('%10s = %-10s' % ('spam', 123.4567))

#  Числа с плавающей точкой
print('%e, %.3e, %g' % (3.14159, 3.14159, 3.14159))
print('%f, %.2f, %06.2f' % (3.14159, 3.14159, 3.14159))
