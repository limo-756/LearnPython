import collections
from random import choice

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


suit_values = dict(spades=3, hearts=2, diamond=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':
    print("Card : ", Card)
    beer_card = Card('7', 'diamond')
    print("beer_card : ", beer_card)
    deck = FrenchDeck()
    print("Length of deck : ", len(deck))
    print("First Card : ", deck[0])
    print("Last Card : ", deck[-1])
    print("Random Card : ", choice(deck))
    print("print first 3 cards : ", deck[:3])
    print("print all ace : ", deck[12::13])
    print("IS hearts Queen in deck : ", Card('Q', 'hearts') in deck)
    print("IS beasts 7 in deck : ", Card('7', 'beasts') in deck)
    for card in sorted(deck, key=spades_high):
        print(card)
