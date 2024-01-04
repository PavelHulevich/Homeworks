# Задание 1:
# Напишите программу, которая принимает на вход строку, содержащую номер телефона (11
# символов, содержащих только цифры) и выводит его в международном формате "+375 (xx)
# xxx-xx-xx", используя форматирование строк. Например, если на вход подана строка
# "80299098425", то на выходе должна быть строка "+375 (29) 909-84-25". Программа должна
# использовать 3 метода форматирования (f-strings, % и format) вывести 3 отформатированные
# строки.

def print_telephone_number(telephone):
    print(f'+375 ({telephone[2:4]}) {telephone[4:7]}-{telephone[7:9]}-{telephone[9:]}')
    print('+375 (%s) %s-%s-%s' % (telephone[2:4], telephone[4:7], telephone[7:9], telephone[9:]))
    print('+375 ({}) {}-{}-{}'.format(telephone[2:4], telephone[4:7], telephone[7:9], telephone[9:]))

    # еще один вариант вывода списка
    telephone_list = telephone[2:4], telephone[4:7], telephone[7:9], telephone[9:]
    print('+375 (%s) %s-%s-%s' % telephone_list)

telephone_in = '80299098425'
print_telephone_number(telephone_in)
