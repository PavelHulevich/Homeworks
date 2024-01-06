# Задание 10*:
# Напишите программу, которая принимает на вход строку, содержащую слово на английском
# языке, и выводит его в форме множественного числа, используя форматирование строк.
# Например, если на вход подана строка "cat", то на выходе должна быть строка "cats". Если
# слово заканчивается на s, x, z, ch или sh, то нужно добавить es. Например, если на вход
# подана строка "box", то на выходе должна быть строка "boxes". Если слово заканчивается на
# y, предшествующий которому согласный звук, то нужно заменить y на ies. Например, если на
# вход подана строка "lady", то на выходе должна быть строка "ladies". В остальных случаях
# просто добавьте s.

# def add_plural_ending(word):
# # Вариант с сечением строк
#     if word[-1:] in ['s', 'x', 'z'] or word[-2:] in ['ch', 'dh']:
#         return word + 'es'
#     elif word[-1:] == 'y' and word[-2:-1] in consonants_list:         # если в конце слова 'y' после согласной
#         return word[:-1] + 'ies'
#     else:
#         return word + 's'


def addition_plural_ending(word):
    # Вариант с анализом конца строки
    if word.endswith(('s', 'x', 'z')) or word.endswith(('ch', 'dh')):
        word += 'es'
    elif word.endswith('y') and word[-2:-1] in consonants_list:  # если в конце слова 'y' после согласной
        word = word[:-1] + 'ies'
    else:
        word += 's'
    return word


def printing_formatted_results(str_in, str_out):
    print(f'Вывод форматированием f-строкой:      {str_in} ==> {str_out}')
    print('Вывод форматированием ' + chr(37) + '-способом:     %s ==> %s' % (str_in, str_out))
    print('Вывод форматированием через.format:   {} ==> {}'.format(str_in, str_out))


CONSONANTS = 'b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, z'  # согласные
consonants_list = CONSONANTS.split(', ')  # в список без запятых

string_in = 'lady'
string_plural = addition_plural_ending(string_in)
printing_formatted_results(string_in, string_plural)
