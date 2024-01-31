#  Синтаксис открытия файла
#  f = open(file_name, access_mode)
#  access_mode:
# r Только для чтения.
# w   Только для записи. Создаст новый файл, если не найдет с указанным именем.
# rb  Только для чтения (бинарный).
# wb  Только для записи (бинарный). Создаст новый файл, если не найдет с указанным именем.
# r+  Для чтения и записи.
# rb+ Для чтения и записи (бинарный).
# w+  Для чтения и записи. Создаст новый файл для записи, если не найдет с указанным именем.
# wb+ Для чтения и записи (бинарный). Создаст новый файл для записи, если не найдет с указанным именем.
# a   Откроет для добавления нового содержимого. Создаст новый файл для записи, если не найдет с указанным именем.
# a+  Откроет для добавления нового содержимого. Создаст новый файл для чтения записи, если не найдет с указанным именем.
# ab  Откроет для добавления нового содержимого (бинарный). Создаст новый файл для записи, если не найдет с указанным именем.
# ab+ Откроет для добавления нового содержимого (бинарный). Создаст новый файл для чтения записи, если не найдет с указанным именем.

f = open('some_file.txt')
#  не прочитали файл, просто создали объект файла
print(type(f))
#  прочитали файл
print(*f)

f = open('some_file.txt')

#  файл надо обязательно закрыть
#  способ 1:
f.close()


#  способ 2 - довольно экзотический:
#  finally выполнится всегда
try:
    f = open('some_file.txt')
finally:
    f.close()

#  способ 2.1 - вот так делают уже чаще:
try:
    f = open('some_file.txt')
except Exception:
    pass
finally:
    f.close()

#  способ 3 - так делают почти всегда:
with open('some_file.txt') as f:
    f.readline()

#  with - контектстный менеджер
#  в его протоколе 2 метода - открыть ресурс и закрыть ресурс
#  по этому явно не надо закрывать файл, with сделает это за нас
#  менеджер контекста можно использовать не только с файлами,
#  а с любым ресурсом который надо открыть и закрыть (например, соединение с базой данных)


f = open('some_file.txt')
#  Функция read() используется для чтения содержимого файла после открытия его в режиме чтения (r)
print(f.read())

#  Общий синтаксис file.read(size)
#  file = объект файла
#  size = количество символов, которые нужно прочитать. Если не указать, то файл прочитается целиком.

f = open('some_file.txt')
# чтение 7 символов
f.read(7)

#  Функция readline() используется для построчного чтения содержимого файла
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())


f = open('some_file.txt')


f = open('some_file.txt')
#  В Python возможно узнать текущую позицию в файле с помощью функции tell().
#  Таким же образом можно изменить текущую позицию командой seek().
print(f.read(6))
print(f.tell())
f.seek(0)
print(f.read(6))


print('==================')


f = open('xyz.txt', 'w')
#  Функция write() используется для записи в файлы Python, открытые в режиме записи.
f.write('Hello \n World')
f.close()


#  для работы с объектами файловой системы используется модуль os
#  можем создавать директории, обходить дирректории, менять права на чтейние/запись/выполнения файла и т.д.
import os

#  Функция rename() используется для переименовывания файлов
#  os.rename(src, dest)

os.rename("xyz.txt", "abc.txt")


#  Чтение из файла по строчкам:
with open('some_file.txt') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)


#  Запись в файл по строчно:
f = open("foo.txt", "w")
f.writelines(['1'])
f.writelines(["cat\n", "dog\n"])
f.writelines(["cat\n", "dog\n"])
f.close()

#  Запись в файл:
f = open("foo2.txt", "w")
f.write('1cat\ndog\ncat\ndog\n')
f.close()

print('==================')

f = open("foo.txt")
print(f.readline())  # 'cat\n'
print(f.readline())  # 'dog\n'
print(f.readline())  # ''
f.close()
#  Вместо вызова readline можно сразу итерироваться по объекту файла
f = open("foo.txt")
for l in f:
    print(l)

f.close()

#  Можно пользоваться генераторами, для обработки файла по строчно
def file_reader2(file_name):
    f = open('some_file.txt')
    for row in f:
        yield row

    print('close')
    f.close()


#  вместо
#  f = open('some_file.txt')
#  for row in f:
#  лучше использовать контекстный менеджер
def file_reader2(file_name):
    with open('some_file.txt') as f:
        for row in f:
            yield row


file_gen = file_reader2("some_file.txt")
row_count = 0

for row in file_gen:
    row_count += 1

print(f"Row count is {row_count}")


# А вот так прочитаем весь файл сразу, но будем обрабатывать его по строчно
def file_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result

file_gen = file_reader("some_file.txt")
row_count = 0

for row in file_gen:
    row_count += 1

print(f"Row count is {row_count}")
