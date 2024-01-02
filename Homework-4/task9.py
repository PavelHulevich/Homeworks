# Задание 9:
# Реализуйте итератор для колоды 52 карт. Итератор должен вывести все карты в виде строки
# “{название масти} {ранг}”.
class CardDeck:
    def __init__(self):
        self.index_suits = 0
        self.index_ranks = -1
        self.length = 52
        self.suits = ['clubs', 'diamonds', 'hearts', 'spades']
        self.ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

    def __iter__(self):
        return self

    def __next__(self):
        self.index_ranks += 1
        if self.index_ranks <= 12:
            return '{' + self.suits[self.index_suits] + '} {' + str(self.ranks[self.index_ranks]) + '}'
        self.index_ranks = -1
        self.index_suits += 1
        if self.index_suits >= 4:
            raise StopIteration
        return self.__next__()


deck = CardDeck()
for x in deck:
    print(x)
