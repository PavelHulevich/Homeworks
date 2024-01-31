from gun import Gun
from tank import Panzer

player1 = Panzer('ИС-2', Gun(122, 40), 90, 600)
player2 = Panzer('Тигр', Gun(88, 55), 120, 650)


AMMO_TYPES = ['фугасный', 'кумулятивный', 'подкалиберный']
ARMOUR_TYPES = ['гомогенная', 'разнесенная', 'комбинированная']


while True:
    # ================================= ХОД ПЕРВОГО ИГРОКА =========================================
    print('========== Игрок 1 ============>')
    selected_ammo = -1
    while player1.loaded_ammo == None:
        while (selected_ammo < 0 or selected_ammo > 2):
            print('Выбрать снаряд:')
            print('0 - фугасный')
            print('1 - кумулятивный')
            print('2 - бронебойный')

            selected_ammo = int(input())

        player1.load_gun(AMMO_TYPES[selected_ammo])

    selected_armour = -1
    while (selected_armour < 0 or selected_armour > 2):
        print('Выбрать броню:')
        print('0 - гомогенная')
        print('1 - разнесенная')
        print('2 - комбинированная')

        selected_armour = int(input())

    player1.select_armour(ARMOUR_TYPES[selected_armour])
    print('\n')
    print(f'Игрок 1 - текущее состояние: {player1}')
    print('\n')
    print(f'Нажмите Enter для выстрела')
    command = input()

    player1.shoot()

    # ================================= ХОД ВТОРОГО ИГРОКА =========================================
    print("========== Игрок 2 ============>")
    selected_ammo = -1
    while player2.loaded_ammo == None:
        while (selected_ammo < 0 or selected_ammo > 2):
            print('Выбрать снаряд:')
            print('0 - фугасный')
            print('1 - кумулятивный')
            print('2 - бронебойный')

            selected_ammo = int(input())

        player2.load_gun(AMMO_TYPES[selected_ammo])

    selected_armour = -1
    while (selected_armour < 0 or selected_armour > 2):
        print('Выбрать броню:')
        print('0 - гомогенная')
        print('1 - разнесенная')
        print('2 - комбинированная')

        selected_armour = int(input())

    player2.select_armour(ARMOUR_TYPES[selected_armour])

    print('\n')
    print(f'Игрок 2 - текущее состояние: {player2}')
    print('\n')
    print(f'Нажмите Enter для выстрела')
    command = input()

    player2.shoot()
