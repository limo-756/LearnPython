import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = list(str(n) for n in range(2, 11)) + list('JQKA')
    suits = 'spades diamond clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def set_card(deck, position, card):
        deck._cards[position] = card

    __setitem__ = set_card

if __name__ == '__main__':
    deck = FrenchDeck()
    random.shuffle(deck)
    print([a for a in deck])