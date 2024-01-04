# Hw5_task9.py
# Напишите программу преобразующую строку NRZI кода (состоящая из символов _, ‾ и |). В
# строку двоичного кода, а затем этот двоичный код в int, используя только методы для работы
# со строками. После преобразования всех NRZI кодов в числа, их необходимо сложить и
# вывести. Программа должна использовать 3 метода форматирования (f-strings, % и format)
# вывести 3 отформатированные строки.
# Символы |¯ и |_ соответствуют 1, а _ и ¯ соответствуют 0.

nrzi_list_in = [
    '|¯¯|_|¯¯¯¯¯|_|¯|_',
    '|¯¯¯¯¯¯|___|¯|___|¯',
    '|¯|_|¯|______|¯¯|_',
    '|¯|__|¯¯|___|¯|__|¯']                  # список строк с NRZI-кодом


def converting_nrzi_to_binary(nrzi):
    # перевод строки с NRZI-кодом в двоичный код текстом без '0b'
    binary = ''
    index_char = 0
    while index_char < len(nrzi):
        if nrzi[index_char] == '|':
            binary += '1'
            index_char += 2
        else:
            binary += '0'
            index_char += 1
    return binary


def printing_formatted_results(nrzi, binary):
    print(f'NRZI-код:  {nrzi:<20} соответствует двоичному: 0b{binary:>016} / десятичному:  {int(binary, 2):<6}')


summ = 0
for nrzi_current in nrzi_list_in:                             # перебираем строки с NRZI-кодом в списке с кодами
    binary_current = converting_nrzi_to_binary(nrzi_current)  # перевод текущей строки в двоичный вид
    summ = summ + int(binary_current, 2)                      # суммируем содержимое кодов
    printing_formatted_results(nrzi_current, binary_current)

print(f'Сумма чисел переданных кодами: {summ}')
print('Сумма чисел переданных кодами: %s' % summ)
print('Сумма чисел переданных кодами: {}'.format(summ))
