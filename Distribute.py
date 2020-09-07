from Shuffle import shuffle
from Entities import Player
from Entities import Table


def set_players_and_table():
    players = [Player(1), Player(2), Player(3), Player(4)]
    table = Table()
    cards = shuffle()
    for _ in range(0, 4):
        for j in range(0, 4):
            players[j].giveCard(cards.pop(0))

    for i in range(0, 4):
        table.giveCard(cards.pop(0))

    return players, table, cards


def give_players_cards(players, cards):
    for _ in range(0, 4):
        for j in range(0, 4):
            players[j].giveCard(cards.pop(0))