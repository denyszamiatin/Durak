import random

# Unicode characters for suits
SUITS = [u'\u2660', u'\u2665', u'\u2666', u'\u2663']
RANKS = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


def create_new_deck():
    deck = []
    for suit in SUITS:
        for rank in RANKS:
            deck.append(suit + rank)
    return deck


def shuffle_deck(deck):
    random.shuffle(deck)


deck = create_new_deck()
print(deck)
print(len(deck))
shuffle_deck(deck)
print(deck)
