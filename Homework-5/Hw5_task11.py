# Задание 11**:
# Решите задание 3 используя Counter.

from collections import Counter


def print_result(sent_nbr, word_cnt):
    print(f'Вывод форматированием f-строкой:      Sentence {sent_nbr} has {word_cnt:2} words.')
    print('Вывод форматированием %s-способом:     Sentence %s has %2s words' % (chr(37), sent_nbr, word_cnt))
    print('Вывод форматированием через .format:  Sentence {} has {:2} words'.format(sent_nbr, word_cnt))


string_in = ('Python is an easy to learn language. It has many applications in various fields. '
             'You can use it for web development, data analysis, machine learning, and more.')
sentences_list = string_in.split('. ')       # список предложений из строки
sentences_counter = Counter(string_in)       # образуем счетчик символов всего введенного текста
sent_count_all = sentences_counter['.']      # количество предложений равно количеству точек

for index in range(sent_count_all):          # перебираем предложения
    words = Counter(sentences_list[index])   # образуем счетчик символов текущего предложения
    word_count = words[' '] + 1              # количество слов = пробелы перед каждым словом + одно первое слово
    print_result(index + 1, word_count)
