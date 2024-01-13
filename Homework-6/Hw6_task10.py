"""
Задание 10:
Дана строка состоящая из символов '(', ')', '{', '}', '[' и ']'. Напишите программу, которая
определяет, является ли строка допустимой. Входная строка допустима, если:
• Открытые скобки должны быть закрыты скобками того же типа.
• Открытые скобки должны быть закрыты в правильном порядке.
• Каждой закрытой скобке соответствует открытая скобка того же типа.
"""


def checking_parenth_str(string_in):
    # Проверка скобок на допустимость. На выходе True - если нет ошибок
    open_parentheses = ['(', '[', '{']
    pair_parentheses = {'(': ')', '[': ']', '{': '}'}
    string_list = list(string_in)
    stack = []
    no_error = True  # Флаг отсутствия ошибок
    for parenth in string_list:
        if parenth in open_parentheses:    # Если скобка открывающая.
            stack += parenth           # То добавляем ее в стек не закрытых скобок.
            continue
        if not stack:                  # Если скобка закрывающая, но стек открывающих скобок пуст.
            no_error = False           # То лишняя закрывающая скобка. Флаг ошибки. Выход.
            break
        elif parenth != pair_parentheses[stack[-1]]:    # Если скобка закрывающая, но не совпадает с верхней в стеке.
            ...                                     # То скобка другого вида. Флаг ошибки. Выход
            no_error = False
            break
        else:                       # Скобка закрывающая и совпадает с верхней в стеке
            stack = stack[:-1]      # То ОК. Убираем верхний элемент из стека. Идем на следующей элемент списка скобок
    if stack:                       # Если после итерации всей строки стек незакрытых скобок НЕ пуст
        no_error = False            # То была лишняя открытая скобка. Флаг ошибки. Выход
    return no_error


def input_parenth():
    # Ввод скобок с клавиатуры с контролем. На выходе строка со скобками.
    all_parentheses = ['[', ']', '{', '}', '(', ')']
    while True:
        parenth_str = input('Введите строку содержащую только символы скобок "[]{}()" :')
        if all((i in all_parentheses for i in parenth_str)):
            return parenth_str
        print('Введены неверные символы. Повторите ввод.\n')


while True:
    parenth_string = input_parenth()
    is_parenth_ok = checking_parenth_str(parenth_string)
    if is_parenth_ok:
        print(f'Строка {parenth_string} является допустимой')
    else:
        print(f'Строка {parenth_string} является НЕ допустимой')
