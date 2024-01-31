"""
while проверка:
    операторы
    if проверка: break           # Выход из цикла с пропуском else, если есть
    if проверка: continue      # Переход на проверку в начале цикла
else:
    операторы                     # Выполняется, если не было break

"""

#  Continue - вернулись в начало, пропустили операторы после continue
i = 0
str1 = 'Python'
while i < len(str1):
    if str1[i] == 'a' or str1[i] == 't':
        i += 1
        continue
    print('Current Letter :', str1[i])
    i += 1


x = 10
while x:
    x -= 1
    if x % 2 != 0: continue
    print(x, end=' ')


#  Поменяли условие и сократили код, выкинув continue
x = 10
while x:
    x -= 1
    if x % 2 == 0:
        print(x, end=' ')


#  break - прервали цикл
i = 0
str1 = 'Python'
while i < len(str1):
    if str1[i] == 't':
        i += 1
        break

    print('Current Letter :', str1[i])
    i += 1


#  pass - пустой оператор, ничего не делает
str1 = 'Python'
i = 0
while i < len(str1):
    pass
    print('Value of i :', i)


i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("The while loop exhausted")


i = 1
while i <= 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print("The while loop exhausted")


i = 1
while True:
    print(i)
    i += 1

    if i > 5:
        break
