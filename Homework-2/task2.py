#task2.py
import math

a = int(input('Введите значение первой переменной = '))
b = int(input('Введите значение второй переменной = '))
c = int(input('Введите значение третьей переменной = '))
result = abs(a-c)*(a**2+b**2-c)*3/((b+c)*2*math.sqrt(b+c))
print(f'{result:6.4}')
