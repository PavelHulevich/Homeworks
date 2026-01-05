# Only even numbers
# Напишите программу, которая считывает последовательность из 10 целых чисел и определяет, является ли каждое из них чётным или нет.

flag = True

for _ in range(10):
    flag *= not int(input()) % 2
if flag:
    print('YES')
else: print('NO')