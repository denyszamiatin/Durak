import random

# Unicode characters for suits
SUITS = [u'\u2660', u'\u2663', u'\u2666', u'\u2665']
RANKS = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
DEAL = 6
SUIT, RANK =0, 1

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


def get_player_card(number_player, card_move):
    return players_cards[number_player].pop(card_move)


def move(number_player):
    print('You cards:', display_card(number_player))
    card_move = int(input('Enter the card number for the move ')) - 1
    return get_player_card(number_player, card_move)

move(get_first_player())


def compare_with_trump(card1, card2):
    return card1[SUIT] == trump[SUIT] and card2[SUIT] != trump[SUIT]


def consider_trump(card1, card2):
    if card1[SUIT] == card2[SUIT]:
        return RANKS.index(card1[RANK:]) > \
               RANKS.index(card2[RANK:])
    if card2[SUIT] != trump[SUIT]:
        raise ValueError
    return compare_with_trump(card2, card1)


print(consider_trump (move(get_first_player()), move(get_first_player()+1)))
