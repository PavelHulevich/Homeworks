from typing import Any, List, Tuple, Dict, Optional, Union

#  Динамическая типизация, значение age сначала является int, но позже мы меняем его на str.
#  Каждая переменная может представлять любое значение в любой точке программы.

age = 21
print(age)

age = 'Twenty one'
print(age)

"""
то же самое на языке со статической типизацией, например на Java вызывает ошибку
int age = 21;
System.out.print(age);
age = "Twenty One";
System.out.print(age);
переменная age уже зарезервирована под число, нельзя в нее записать данные другого типа

Но можно преобразовать данные одного типа в другой
int ageNum = 21;
System.out.print(ageNum);
String ageStr = ageNum.toString();
System.out.print(ageStr);
"""

#  Аннотации типов – это новая возможность, позволяющая добавлять подсказки о типах переменных.
#  Они используются, чтобы информировать разработчика, каким должен быть тип переменной.


new_age: int = 5  # при объявлении переменной добавляется int, чтобы показать, что переменная должна иметь тип int.
print(new_age)


#  Аннотации типов никак не влияют на время выполнения программы. Они игнорируются интерпретатором

#  Мы видим, что делает эта функция, но знаем ли мы, какими должны быть a, b или times?
def mystery_combine(a, b, times):
    return (a + b) * times

print(mystery_combine(2, 3, 4))
print(mystery_combine('Hello ', 'World! ', 4))


#  Используя аннотации типов, мы можем явно указать аргументы каких типов принимает функция - a: str, b: str, times: int
#  И какой тип данных возвращает функция -> str:
def mystery_combine(a: str, b: str, times: int) -> str:
    return (a + b) * times


#  Вызов функции с аргументами других типов все еще возможен, интерпритатор никак нас не ограничивает.
#  Но редактор кода предупреждает о том, что мы передаем аргументы не верных типов
print(mystery_combine(2, 3, 4))
print(mystery_combine('Hello ', 'World! ', 4))


#  В случаях сложнее чем простые типы данных используется модуль typing
#  В нем описаны типы для аннотирования любой переменной любого типа.
#  Он поставляется с предварительно загруженными аннотациями типов, таких как Dict, Tuple, List, Set и т.д.


#  names должен быть списком строк, функция возвращает None
def print_names(names: List[str]) -> None:
    for student in names:
        print(student)


x = print_names(['1', '2'])

#  функция вернула None
print(type(x))


#  Подсказка типа Dict [str, float] сообщает нам, что оценки должны быть словарем,
#  где ключи являются строками, а значения — числами с плавающей запятой.
def print_name_and_grade(grades: Dict[str, float]) -> None:
    for student, grade in grades.items():
        print(student, grade)


print_name_and_grade({2: 1})  # не верный вызов функции из-за передачи данных других типов
print_name_and_grade({'2': 1.1})


#  Псевдонимы типов используются для создания пользовательских имен типов
#  Допустим, вы работаете с группой точек [x, y] в виде кортежей.
#  Тогда можно использовать псевдоним для сопоставления типа Tuple с типом Point.
Point = Tuple[int, int]


#  Создание функции, принимающей список значений Point
def print_points(points: List[Point]) -> None:
    for point in points:
        print("X:", point[0], " Y:", point[1])


#  Если функция возвращает несколько значений в виде кортежа,
#  возвращаемый результат функции оформляется так: typing.Tuple[<тип 1>, <тип 2>, ...]
def get_api_response() -> Tuple[int, int]:
    return 1, 2


#  Если аргумент функции принимает значения различных типов, можно использовать typing.Optional или typing.Union
#  Optional, если значение будет либо определенного типа, либо исключительно None.
#  Optional[int] == Union[int, None]
#  Optional[int, str] == Union[int, str, None]


#  Аргумент some_num может быть ИЛИ int ИЛИ None
def try_to_print(some_num: Optional[int]):
    if some_num:
        print(some_num)
    else:
        print('Значение было None!')


try_to_print(1)
try_to_print(None)
try_to_print('www')


#  Когда значение может принимать более конкретные типы, используйте Union
#  Аргумент grade может быть ИЛИ int ИЛИ str
def print_grade(grade: Union[int, str]):
    if isinstance(grade, str):
        print(grade + ' процентов')
    else:
        print(str(grade) + '%')


#  Когда мы не знаем какой тип данных будет передан в функцию, то используется тип Any
#  Использование Any является дурным тоном, потому что это равнозначно отсутствию аннотации
def func(**kwargs: Dict[Any, Any]) -> Any:
    return


