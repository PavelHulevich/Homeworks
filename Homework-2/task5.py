#task5.py

a = int(input('Введите четырехзначаное число = '))
a_reverse = a%1000%100%10*1000+a%1000%100//10*100+a%1000//100*10+a//1000
print(a_reverse, a-a_reverse, sep='\n')
