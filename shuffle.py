#This could be used as a deck and shuffle#
def shuffle():
    import random
    i = 0
    while i <= 5:
        rank = random.choice(('Ace', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'))
        suit = random.choice(('Club', 'Diamond', 'Heart', 'Spade'))
        card = (f"{rank} of {suit}")
        i += 1
        print(card)
print(shuffle())