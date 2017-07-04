import random

# Unicode characters for suits
SUITS = [u'\u2660', u'\u2663', u'\u2666', u'\u2665']
RANKS = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
DEAL = 6


def create_new_deck(suits=SUITS):
    deck = []
    for suit in suits:
        for rank in RANKS:
            deck.append(suit + rank)
    return deck


def shuffle_deck(deck):
    random.shuffle(deck)

# players - number of players
players = 3


def deal_cards(deck, players_number):
    players_cards = []
    for number in range(players_number):
        player_cards = deck[:DEAL]
        deck = deck[DEAL:]
        players_cards.append(player_cards)
    return players_cards


def display_card(player_cards):
    for card in player_cards:
        print(card, end=" ")
    print()


deck = create_new_deck()
#print(deck)
#print(len(deck))
shuffle_deck(deck)
#print(deck)
players_cards = deal_cards(deck, players)
for card in players_cards:
    display_card(card)


def elect_trump():
    return deck.pop(-1)

trump = elect_trump()
print('Trump is', trump)


def rotate_suits(suits, trump):
    """
    >>> rotate_suits([0, 1, 2, 3], 2)
    [2, 3, 0, 1]
    >>> rotate_suits([0, 1, 2, 3], 0)
    [0, 1, 2, 3]
    >>> rotate_suits([0, 1, 2, 3], 3)
    [3, 0, 1, 2]
    >>> rotate_suits([0, 1, 2, 3], 4)
    Traceback (most recent call last):
    ...
    ValueError
    """
    if trump not in suits:
        raise ValueError
    while suits[0] != trump:
        suits.append(suits[0])
        suits.pop(0)
    return suits


trumped_suits = rotate_suits(SUITS[:], trump[0])
print(trumped_suits)


def get_first_player():
    print(create_new_deck(trumped_suits))
    for card in create_new_deck(trumped_suits):
        print(card)
        for player_number, cards in enumerate(players_cards):
            if card in cards:
                return player_number


print ('First to go is player No', get_first_player())

#Assume Issue No 8 provides us with input_card_one and input_card_two
#until then dummies are:
input_card_one = SJ
input_card_two = SA

def consider_trump (input_card_one, input_card_two):
    if input_card_one[0]==trump[0] and input_card_two [0]!=trump[0]:
          return True
    if input_card_one[0]!=trump[0] and input_card_two [0]==trump[0]:
          return False
    elif input_card_one[0] != input_card_two [0]:
            return True
    else:
            return RANKS.index (input_card_one[1:]) >RANKS.index (input_card_two[1:])

print consider_trump (input_card_one, input_card_two)
