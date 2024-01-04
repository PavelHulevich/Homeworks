# Hw5_task8.py
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


def cleaning_morze(morze_noise_fn):
    morze_clean_fn = ''
    for char in morze_noise_fn:
        if char == '-' or char == '.' or char == ' ':
            morze_clean_fn += char
    return morze_clean_fn


def morze_to_text(morze_clean_fn):
    text_out_fn = ''
    for morze_pointer in range(0, len(morze_clean_fn), 4):
        text_out_fn += alphabet[morze_clean_fn[morze_pointer:morze_pointer + 4]]
    return text_out_fn


morze_noise = ('-   .   .sdfs.. Dfgh-   --- .-3467- 4'
               '--- .   ... +%--- --- лоууоу-...--.-.   -.  ..  .   ')  # телеграфное сообщение с помехами
morze_clean = cleaning_morze(morze_noise)
text_out = morze_to_text(morze_clean)
print(f'{text_out}')
print('%s' % text_out)
print('{}'.format(text_out))
