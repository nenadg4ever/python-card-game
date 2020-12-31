from itertools import product 
import random

class Card(object):

    FACES = {11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        value = self.FACES.get(self.rank, self.rank)
        return "{0} of {1}".format(value, self.suit)

    def __lt__(self, other):
        return self.rank < other.rank

class Deck(object):

    def __init__(self, ranks=None, suits=None):
        if ranks is None:
            ranks = range(2, 15)
        if suits is None:
            suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
##        self.deck = [Card(r, s) for r, s in product(ranks, suits)]
        self.deck = []
        for r in ranks:
            for s in suits:
                self.deck.append(Card(r, s))

    def deal(self, n):
        return random.sample(self.deck, n)

deck = Deck()
hand = deck.deal(3)
print(" - ".join(map(str, hand)))
if min(hand[0], hand[1]) < hand[2] < max(hand[0], hand[1]):
    print("Winner!")
else:
    print("Loser.")