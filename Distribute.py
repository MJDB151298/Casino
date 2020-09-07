from Shuffle import shuffle
from Entities import Player
from Entities import Table

# funcion set_players_and_table: Les da a cada jugador 4 cartas y pone en la mesa 4 cartas
# RETORNO
# retorna los 4 jugadores con sus cartas inciales, la mesa con sus cartas, y las cartas del mazo restantes.
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

# funcion give_players_cards: les da a cada jugador 4 cartas.
# PARAMETROS
# players: los jugadores que se encuentran jugando.
# cards: el mazo de cartas.
# RETORNO
# no tiene retorno, esto actualiza los jugadores y las cartas solamente.
def give_players_cards(players, cards):
    for _ in range(0, 4):
        for j in range(0, 4):
            players[j].giveCard(cards.pop(0))