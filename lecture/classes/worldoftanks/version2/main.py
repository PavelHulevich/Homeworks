from gun import Gun
from tank import Panzer

player1 = Panzer('ИС-2', Gun(122, 40), 90, 600)
player2 = Panzer('Тигр', Gun(88, 55), 120, 650)


while True:
    # ================================= ХОД ПЕРВОГО ИГРОКА =========================================
    print('========== Игрок 1 ============>')
    print('Выбрать снаряд:')
    print('Выбрать броню:')
    print('\n')
    print(f'Игрок 1 - текущее состояние: {player1}')
    print('\n')
    print(f'Нажмите Enter для выстрела')
    command = input()

    # ================================= ХОД ВТОРОГО ИГРОКА =========================================
    print("========== Игрок 2 ============>")
    print('Выбрать снаряд:')
    print('Выбрать броню:')
    print('\n')
    print(f'Игрок 2 - текущее состояние: {player1}')
    print('\n')
    print(f'Нажмите Enter для выстрела')
    command = input()
