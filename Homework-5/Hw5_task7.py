# Hw5_task7.py
alphabet = {
    '.-  ': 'А', '-...': 'Б', '.-- ': 'В', '--. ': 'Г',
    '-.. ': 'Д', '.   ': 'Е', '...-': 'Ж', '--..': 'З',
    '..  ': 'И', '.---': 'Й', '-.- ': 'К', '.-..': 'Л',
    '--  ': 'М', '-.  ': 'Н', '--- ': 'О', '.--.': 'П',
    '.-. ': 'Р', '... ': 'С', '-   ': 'Т', '..- ': 'У',
    '..-.': 'Ф', '....': 'Х', '-.-.': 'Ц', '---.': 'Ч',
    '----': 'Ш', '--.-': 'Щ', '-. -': 'Ъ', '-.--': 'Ы',
    '-..-': 'Ь', '. -.': 'Э', '..--': 'Ю', '.-.-': 'Я',
}
alphabet_rev = {}  # Обратный словарь
for key, value in alphabet.items():  # Генерация обратного словаря
    alphabet_rev[value] = key

string_in = 'ТЕСТОВОЕ СООБЩЕНИЕ'
morze_out = ''

for index in string_in:  # перебираем символы в строке
    if index != ' ':     # убираем пробелы
        morze_out += alphabet_rev[index]  # формируем строку с кодом морзе

print(f'{string_in} ==>  "{morze_out}"')
print('%s ==>  "%s"' % (string_in, morze_out))
print('{} ==>  "{}"'.format(string_in, morze_out))
