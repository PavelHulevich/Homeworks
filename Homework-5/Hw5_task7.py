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


def converting_string_to_morze(string):
    morze = ''
    for char in string:  # перебираем символы в строке
        if char != ' ':  # убираем пробелы
            morze += alphabet_rev[char]  # формируем строку с кодом морзе
    return morze


alphabet_rev = {}                    # Обратный словарь
for key, value in alphabet.items():  # Генерация обратного словаря
    alphabet_rev[value] = key

string_in = 'ТЕСТОВОЕ СООБЩЕНИЕ'
morze_out = converting_string_to_morze(string_in)

print(f'{string_in} ==>  "{morze_out}"')
print('%s ==>  "%s"' % (string_in, morze_out))
print('{} ==>  "{}"'.format(string_in, morze_out))
