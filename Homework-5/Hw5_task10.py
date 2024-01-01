# Задание 10*:
# Напишите программу, которая принимает на вход строку, содержащую слово на английском
# языке, и выводит его в форме множественного числа, используя форматирование строк.
# Например, если на вход подана строка "cat", то на выходе должна быть строка "cats". Если
# слово заканчивается на s, x, z, ch или sh, то нужно добавить es. Например, если на вход
# подана строка "box", то на выходе должна быть строка "boxes". Если слово заканчивается на
# y, предшествующий которому согласный звук, то нужно заменить y на ies. Например, если на
# вход подана строка "lady", то на выходе должна быть строка "ladies". В остальных случаях
# просто добавьте s.

string_in = 'lady'
consonants = 'b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, z'  # согласные
consonants_list = consonants.split(', ')                                   # в список без запятых

# Вариант с сечением строк
# if string_in[-1:] in ['s', 'x', 'z'] or string_in[-2:] in ['ch', 'dh']:
#     string_out = string_in + 'es'
# elif string_in[-1:] == 'y' and string_in[-2:-1] in consonants_list:         # если в конце слова 'y' после согласной
#     string_out = string_in[:-1] + 'ies'
# else:
#     string_out = string_in + 's'

# Вариант с анализом конца строки
if string_in.endswith(('s', 'x', 'z')) or string_in.endswith(('ch', 'dh')):
    string_out = string_in + 'es'
elif string_in.endswith('y') and string_in[-2:-1] in consonants_list:      # если в конце слова 'y' после согласной
    string_out = string_in[:-1] + 'ies'
else:
    string_out = string_in + 's'

print(f'Вывод форматированием f-строкой:      {string_in} ==> {string_out}')
print('Вывод форматированием '+chr(37)+'-способом:     %s ==> %s' % (string_in, string_out))
print('Вывод форматированием через .format:  {} ==> {}' .format(string_in, string_out))
