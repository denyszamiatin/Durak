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

# Took MykhayloSharapov code and wrote it as a function
def trump():
    t=random.randint(0,3)
    trump = SUITS[t]
    return trump
print('Trump is',trump())



# players - number of players
players = 5


def issue_cards(players, deck):
    players_cards = []
    for number in range(players):
        player = deck[number:players*6:players]
        players_cards.append(player)
    return players_cards


def display_card(players_cards):
    for card in players_cards[0]:
        print(card, end=" ")


deck = create_new_deck()
print(deck)
print(len(deck))
shuffle_deck(deck)
print(deck)

