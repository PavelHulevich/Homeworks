class Primes:
    def __init__(self, max):
        self.max = max
        self.number = 1
        self.length = 52
        self.suits = ['clubs', 'diamonds', 'hearts', 'spades']
        self.ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.number >= self.max:
            raise StopIteration

        return self.number


primes = Primes(40)
print(primes)

for x in primes:
    print(x)
