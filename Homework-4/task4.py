# Задание 4:
# Напишите программу, которая читает строку, содержащую имя и фамилию человека, и
# выводит на экран приветствие в зависимости от пола человека. Если фамилия оканчивается
# на "а" или "я", то считать, что человек женского пола, иначе - мужского. Для решения
# используйте pattern matching.
# Например, если вводится "Анна Смирнова", то программа должна вывести "Здравствуйте,
# госпожа Смирнова". Если вводится "Иван Петров", то программа должна вывести
# "Здравствуйте, господин Петров"

name = input('Введите Имя и Фамилию человека: ')

match name[-1:]:
    case ('а' | 'я'):
        print("Здравствуйте, госпожа ", name)
    case _:
        print("Здравствуйте, господин ", name)
