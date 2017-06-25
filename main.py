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

#Issue 5: select Trump        

def elect_trump():
    trump = str(deck[35])[0]
    return str(trump)

trump = elect_trump()
print ('Trump is', trump)

# Issue 6: Determine first to play.
# Let's arrange the deck in the order of human search for the smallets trump on hands.

trumped_SUITS = SUITS[:]

i = 0
while trumped_SUITS [i] != trump:
        trumped_SUITS.append (trumped_SUITS [i])
        trumped_SUITS.pop (i)

trumped_deck = []

for i in (trumped_SUITS):
    for j in (RANKS):
        trumped_deck.append (i+j)

i = 0
while trumped_deck[i] not in (players_cards):
    i+=1

print ('First to go is player No',int((players_cards.index (trumped_deck[i])+1)//6.001+1),'!')

