vacuum_cur=float(input('Введите установленное значение разрежения: '))
volume_cur=float(input('Введите измеренное значение набираемого объема жидкости:  '))
volume_req=float(input('Введите требуемое значение набираемого объема жидкости: '))

print('Необходимое значение разрежения: ', round((vacuum_cur / volume_cur * volume_req)), 'mBar')