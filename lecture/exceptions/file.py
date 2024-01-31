"""
Исключения помогают обрабатывать непредвиденные ошибки и предотвращать критические сбои.
Когда возникает исключение интерпретатор Python останавливает текущий процесс и передает управление обработчику
исключений. Если его не удается обработать или обработчика такого исключения нет, программа аварийно завершается.

В Python исключения обрабатываются при помощи инструкции try.
Критическая операция, которая может вызвать исключение, помещается внутрь блока try.
А код, при помощи которого это исключение будет обработано, — внутрь блока except.


try:
    # do something
    pass
except ValueError:
    # handle ValueError exception
    pass
except (TypeError, ZeroDivisionError):
    # handle multiple exceptions
    # TypeError and ZeroDivisionError
    pass
except:
    # handle all other exceptions
    pass
else:
    pass
finally:
    pass


"""

# Для получения типа исключения импортируем модуль sys
import sys

randomList = ['a', 0, 2]
for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)  #  Если исключений не возникает, блок except пропускается
                          #  программа продолжает выполнятся обычным образом
        print(entry, r)
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()


#  все исключения наследуются из базового класса Exception, мы можем переписать наш код следующим образом
randomList = ['a', 0, 2]
for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        print(entry, r)
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
        print()


#  мы можем определить, какие именно исключения мы будем перехватывать, и как мы их будем обрабатывать.
try:
    # do something
    pass
except ValueError:
    # handle ValueError exception
    pass
except (TypeError, ZeroDivisionError):
    # handle multiple exceptions
    # TypeError and ZeroDivisionError
    pass
except:
    # handle all other exceptions
    pass


"""
Исключение автоматически вызывается, когда во время выполнения программы возникает ошибка. 
Мы можем сами вызвать исключение, используя для этого инструкцию raise.
"""
for i in [10, 0, -5]:
    try:
        a = i
        if a <= 0:
            raise ValueError(f"{a} is not a positive number!")  #  Можно передать значения в исключение для информативности
    except ValueError as ve:
        print(ve)


"""
В некоторых случаях бывает полезным выполнить определенный код в случае, если исключение не было вызвано. 
Для этого можно использовать необязательный блок else вместе с инструкцией try.
Исключения, возникающие в самом блоке else, не будут обработаны в предшествующем ему блоке except.
"""

for i in [1, 4, 0]:
    try:
        num = i
        assert num % 2 == 0
    except:
        print("Число нечетное!")
    else:
        try:
            result = 1/num
            print(result)
        except:
            print("Ошибка")

"""
Инструкция try может также иметь и необязательный блок finally. 
Этот блок кода будет выполнен в любом случае и обычно используется для освобождения внешних ресурсов.
"""


try:
    1/1
except ZeroDivisionError:
    print('Catched ZeroDivisionError')
finally:
    print('Final block')


"""
В Python пользователи могут определять свои собственные исключения, создавая новый класс. 
Этот класс исключений должен прямо или косвенно быть производным от встроенного класса Exception. 
Большинство встроенных исключений также являются производными от этого класса. 
Все пользовательские исключения также должны быть производными от этого класса.
"""


class CustomError(Exception):
    pass


"""
Exception наследуется от BaseException, наследовать наши исключения от BaseException не является хорошим тоном.
С большой долей вероятности оно не будет обработано корректно
"""
class CustomError2(BaseException):
    pass


"""
Пользовательские исключения полезны тем, что их можно вызвать с неправильными или неожиданными входными данными, 
тем самым лучше прояснив ситуацию с кодом, который падает или неправильно работает.
"""
try:
    raise CustomError
except:
    pass
try:
    raise CustomError('AN ERROR')
except:
    pass


"""
CustomError наследуется от класса Exception, а исключение KeyError наследуется от другого класса и 
находится ниже в иерархии наследований. Исключение выше по иерархии наследования - CustomError не может 
перехватиться обработчиком исключения находящимся ниже по иерархии наследования

"""

try:
    try:
        raise CustomError2
    except KeyError:
        print("Не перехватили здесь")
except:
    print("Перехватили здесь")
    pass


class Error(Exception):
    pass


class ValueTooSmallError(Error):
    pass


class ValueTooLargeError(Error):
    pass


number = 10

for i in [1, 20, 10]:
    try:
        i_num = i
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        print("Поздравляю! Вы правильно угадали.")
    except ValueTooSmallError:
        print("Это число меньше загаданного, попробуйте еще раз!\n")
    except ValueTooLargeError:
        print("Это число больше загаданного, попробуйте еще раз!\n")
