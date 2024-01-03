# Задание 3:
# Напишите программу, которая принимает на вход строку, содержащую несколько предложений,
# и выводит количество слов в каждом предложении, используя форматирование строк. Например, если на вход подана
# строка "Python is an easy to learn language. It has many applications in various fields. You can use it for web
# development, data analysis, machine learning, and more.", то на выходе должна быть строка "Sentence 1 has 7 words.
# Sentence 2 has 7 words. Sentence 3 has 13 words.". Программа должна использовать 3 метода форматирования (fstrings,
# % и format) вывести 3 отформатированные строки.

def print_result(sent_nmb, word_cnt):  # Вывод номера предложения и количества слов в нем
    print(f'Вывод форматированием f-строкой:    Sentence {sent_nmb} has {word_cnt} words.')
    print('Вывод форматированием ' + chr(37) + '-способом:   Sentence %s has %s words' % (sent_nmb, word_cnt))
    print('Вывод форматированием через format: Sentence {} has {} words\n'.format(sent_nmb, word_cnt))


string_in = ('Python is an easy to learn language. It has many applications in various fields. '
             'You can use it for web development, data analysis, machine learning, and more.')
sentences_list = string_in.split('. ')                   # Список предложений из строки
for sentence in sentences_list:                         # Перебираем все предложения из списка предложений
    sentence_number = sentences_list.index(sentence) + 1    # Порядковый номер текущего предложения
    words_list = sentence.split(' ')                     # Список слов из текущего предложения
    words_count = len(words_list)                          # Количество слов в текущем предложении
    print_result(sentence_number, words_count)
