"""
Задание 6:
Напишите программу, которая вводит по строкам с клавиатуры двумерный массив и
вычисляет сумму его элементов по столбцам.
"""
while True:
    try:
        rows = int(input('Введите количество строк двумерного массива: '))
        cols = int(input('Введите количество столбцов двумерного массива: '))
        two_dim_list = [[0] * cols for _ in range(rows)]
        sum_cols = [0] * cols
        for i in range(rows):
            row_current = input(f'Введите {cols} элемента строки № {i + 1} , разделяя числа пробелом: ')
            row_current_list = row_current.split(' ')
            for j in range(cols):
                two_dim_list[i][j] = int(row_current_list[j])
                sum_cols[j] += int(row_current_list[j])
    except ValueError:
        print('Введены недопустимые данные. Повторите ввод')
    else:
        break
print('Введен массив: ')
print(i for i in two_dim_list)
    
print('Сумма элементов по столбцам: ', sum_cols)
