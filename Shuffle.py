import random
from Entities import Card

# funcion shuffle: se encarga de construir las 52 cartas y barajarlas.
# RETORNO
# retorna las cartas barajadas.
def shuffle():
    cards = []
    symbols = ['♥', '♦', '♣', '♠']
    for symbol in symbols:
        for i in range(1, 14):
            card = {}
            if i == 1:
                card = {'number': 'A', 'sign': symbol, 'value': i}
            elif i == 11:
                card = {'number': 'J', 'sign': symbol, 'value': i}
            elif i == 12:
                card = {'number': 'Q', 'sign': symbol, 'value': i}
            elif i == 13:
                card = {'number': 'K', 'sign': symbol, 'value': i}
            else:
                card = {'number': i, 'sign': symbol, 'value': i}
            object_card = Card(card['number'], card['sign'], card['value'])
            cards.append(object_card)
    shuffled_cards = []
    for _ in range(0, 52):
        card_size = len(cards) - 1
        if card_size == 0:
            shuffled_cards.append(cards.pop())
        else:
            shuffled_cards.append(cards.pop(random.randrange(card_size)))
    return shuffled_cards
