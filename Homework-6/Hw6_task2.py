"""
Задание 2:
Напишите 2 программы, которые используют цикл for и while для вывода на экран таблицы
умножения от 1 до 10.
"""
print('\nMethod 1\n')
for i in range(1, 11):
    for j in range(1, 11):
        print(f'{j * i:^4}', end=' ')
    print('\n')


print('Method 2\n')
i = 0
while i < 10:
    i += 1
    j = 0
    while j < 10:
        j += 1
        print(f'{j * i:^4}', end=' ')
    print('\n')
