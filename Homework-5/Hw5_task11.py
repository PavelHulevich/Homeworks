# Задание 11**:
# Решите задание 3 используя Counter.

from collections import Counter


def printing_formatted_results(sent_nbr, word_cnt):
    print(f'Вывод форматированием f-строкой:      Sentence {sent_nbr} has {word_cnt:2} words.')
    print('Вывод форматированием %s-способом:     Sentence %s has %2s words' % (chr(37), sent_nbr, word_cnt))
    print('Вывод форматированием через .format:  Sentence {} has {:2} words'.format(sent_nbr, word_cnt))


string_in = ('Python is an easy to learn language. It has many applications in various fields. '
             'You can use it for web development, data analysis, machine learning, and more.')
sentences_list = string_in.split('. ')             # список предложений из строки

for sentence in sentences_list:
    words_counter = Counter(sentence)[' '] + 1
    sentence_number = sentences_list.index(sentence) + 1
    printing_formatted_results(sentence_number, words_counter)
