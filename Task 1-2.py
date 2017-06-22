import random

#Unicod characters for suits#
suit = [u'\u2660', u'\u2665', u'\u2666', u'\u2663']
rang = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def new_deck():
    deck = []
    for m in suit:
        for l in rang:
            card = m + l
            deck.append(card)
#I don't know how to combine two functions, that is why I use random.shufle inside this one#
    random.shuffle(deck)
    return deck
print(new_deck())

"""#This could be used as a deck and shuffle#
def shuffle():
    import random
    i = 0
    while i <= 5:
        rank = random.choice(('Ace', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'))
        suit = random.choice(('Club', 'Diamond', 'Heart', 'Spade'))
        card = (f"{rank} of {suit}")
        i += 1
        print(card)
"""