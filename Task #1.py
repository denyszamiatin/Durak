suit = [u'\u2660',u'\u2665',u'\u2666',u'\u2663']
rang = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
def new_deck () :
    deck = []
    for m in suit :
           for l in rang :
                card = m + l
                deck.append (card)
    return deck
print(new_deck () )