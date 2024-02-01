"""
Замыкания — это функция, которая запоминает значения из своей внешней области видимости,
даже если эта область уже недоступна. Она создается, когда функция объявляется,
и продолжает запоминать значения переменных даже после того, как вызывающая функция завершит свою работу.

Замыкания — это инструмент, который позволяет сохранять значения и состояние между вызовами функций, создавать функции
на лету и возвращать их из других функций.

Замыкание возникает, когда функция объявляется внутри другой функции и использует переменные из внешней функции.
В этом случае внешняя функция создает замыкание, которое хранит ссылку на внешние переменные, используемые во
внутренней функции. Замыкание позволяет внутренней функции получить доступ к этим переменным,
даже если внешняя функция уже завершилась.
"""


"""
Функция outer_function, которая принимает аргумент x и возвращает внутреннюю функцию inner_function. 
Внутренняя функция также принимает аргумент y и возвращает сумму x и y.
"""
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function


#  Мы создаем замыкание closure, вызывая outer_function с аргументом 10.
#  Теперь closure ссылается на inner_function и хранит значение x как 10.
closure = outer_function(10)

#  Вызываем closure с аргументом 5 и выводим результат
print(closure(5))


"""
Замыкание состоит из двух частей:
    • Внешняя функция
    • Внутренняя функция
    
Внутренняя функция имеет доступ к переменным из внешней функции даже после того, как внешняя функция завершила 
свою работу. Это происходит, так как замыкание сохраняет ссылку на эти переменные, а не копирует их значение. 
Так замыкания могут использовать и изменять значения этих переменных между вызовами.
"""


"""
Внутри counter мы определяем переменную count и возвращаем inner. 
Внутренняя функция inner использует переменную count, которая определена во внешней функции counter с 
помощью оператора nonlocal, и увеличивает ее значение на единицу при каждом вызове.
"""
def counter():
    count = 0

    def inner():
        nonlocal count

        count += 1
        return count

    return inner


c1 = counter()
print(c1())
print(c1())
print(c1())


"""
Функция add_number, которая принимает аргумент n и возвращает внутреннюю функцию inner. 
Внутренняя функция inner также принимает аргумент x и возвращает сумму n и x.
Затем мы создаем два замыкания: add_five и add_ten, вызывая add_number с аргументами 5 и 10 соответственно.
"""
def add_number(n):
    def inner(x):
        return x + n

    return inner

add_five = add_number(5)
add_ten = add_number(10)

print(add_five(3))
print(add_five(4))
print(add_ten(5))