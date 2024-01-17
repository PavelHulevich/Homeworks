"""
Задание 2:
Напишите генератор, который симулирует работу автомата по продаже напитков. Генератор
должен принимать словарь drinks, где ключи - названия напитков, а значения - цены.
Генератор должен возвращать сообщения пользователю о выборе напитка, внесении денег и
выдаче сдачи. Используйте метод send для передачи выбора пользователя и внесенной суммы
в генератор.
Пример:
def vending_machine(drinks):
 …
vm = vending_machine({'coffe': 10, 'cola': 20})
next(vm)
Выберите напиток:
coffe - 10 руб.
cola - 20 руб.
vm.send('cola')
Вы выбрали cola. Внесите 20 руб.
vm.send(10)
Недостаточно денег.
"""


def vending_machine(drinks):
    print('Выберите напиток: ')
    for k, v in drinks.items():
        print(f'{k:6} - {v:2} руб.')
    drink = yield
    print(f'Вы выбрали: {drink}.')
    print(f'Внесите {drinks[drink]} руб.')
    money = yield
    print(f'Вы внесли {money} руб.')
    if money < drinks[drink]:
        print('Недостаточно денег\n')
    elif money > drinks[drink]:
        print(f'Ваша сдача: {money - drinks[drink]}.')
        print('Заберите сдачу и напиток\n')
    else:
        print('Заберите напиток\n')
    yield


while True:
    try:
        vm = vending_machine({'coffe': 10, 'cola': 20, 'tea': 5, 'tarhun': 15})
        next(vm)
        vm.send(input())
        vm.send(int(input()))
    except:
        print('Введены неверные данные\n')



