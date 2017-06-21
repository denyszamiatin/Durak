suit = ['s', 'c', 'd', 'h']
rang = ['6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']
def new_deck () :
    deck = []
    for m in suit:
           for l in rang:
                card = m + l
                deck.append (card)
    return deck
print(new_deck())