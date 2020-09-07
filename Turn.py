import Distribute
from Entities import Table


# SYMBOL SHORTCUTS:
# alt + 3: ♥
# alt + 4: ♦
# alt + 5: ♣
# alt + 6: ♠

# funcion start: Inicia el juego llamando a las funciones que reparten las cartas, toman lo que el jugador quiere hacer
# cada turno y sigue corriendo hasta que se determina que el juego ha terminado
def start():
    players, table, cards = Distribute.set_players_and_table()
    last_player_taking = None
    while True:
        if check_game_over(players, table, cards, last_player_taking):
            calculate_winner(players)
            break
        if check_redistribute(players):
                print("Repartiendo cartas nuevamente...")
                Distribute.give_players_cards(players, cards)
        for player in players:
            print(len(cards))
            turn_completed = False
            while turn_completed is False:
                show_table(player, table)
                try:
                    move_type = int(input("1- Descartar\n"
                                    "2- Tomar\n"
                                    "3- Construir\n"
                                    "Eliga lo que hara en su turno: "))
                    if move_type == 1:
                        turn_completed = discard(player, table)
                    elif move_type == 2:
                        turn_completed, last_player_taking = take(player, table)
                    elif move_type == 3:
                        turn_completed = build(player, table)
                    else:
                        print("Opcion no valida")
                except ValueError:
                    print("Opcion no valida")
    print("Gracias por jugar!")


# funcion check_game_over: Determina si los jugadores no tienen mas cartas y no hay mas cartas para repartir.
# PARAMETROS:
# players: Los jugadores.
# table: La mesa del juego.
# cards: las cartas restantes.
# last_player_taking: En casino, cuando el juego se acaba, el ultimo jugador que tomo cartas se queda con lo que hay en la mesa.
# RETORNO:
# True si el juego ha finalizado, False si no.
def check_game_over(players, table, cards, last_player_taking):
    if check_redistribute(players) and len(cards) == 0:
        for player in players:
            if player == last_player_taking:
                for i in range(0, len(table.cards)):
                    for card in table.cards[i]:
                        player.gained_cards.append(card)
        return True
    return False


# funcion calculate_winner: Calcula el puntuaje de todos los jugadores
# PARAMETROS:
# players: Los jugadores.
def calculate_winner(players):
    total_cards = []
    total_spades = []
    for player in players:
        total_cards.append(len(player.gained_cards))
        total_spades.append(len(player.count_spades()))
        player.score += player.big_casino()
        player.score += player.small_casino()
    players[total_cards.index(max(total_cards))].score += 3
    players[total_spades.index(max(total_spades))].score += 1


# funcion check_redistribute: Verifica si hay que entregar 4 cartas mas a los jugadores:
# PARAMETROS:
# players: Los jugadores
# RETORNO:
# True si hay que redistribuir, False si no.
def check_redistribute(players):
    for player in players:
        if len(player.hand_cards) != 0:
            return False
    return True


# funcion show_table: Muestra las cartas de un jugador y la mesa.
# PARAMETROS:
# player: Jugador
# table: Mesa del juego
def show_table(player, table):
    print("Turn Player " + str(player.identifier))
    player.show_cards()
    print("\n")
    print("Table")
    table.print_table()
    print("\n")


# funcion discard: El jugador descarta una de las cartas que tiene en mano y la pone sobre la mesa
# PARAMETROS:
# player: jugador que descartara la carta
# table: mesa del juego.
# RETORNO
# True si el jugador se deshace de la carta.
# False si el jugador decide no descartar y hacer otro tipo de movida.
def discard(player, table):
    player.show_cards()
    card = None
    while card is None:
        card_discarded = input("Escriba la carta que desea remover (si desea hacer otro tipo de jugada, escriba 0): ")
        if card_discarded == '0':
            print("\n")
            return False
        card = player.search_card(card_discarded)
        if card is None:
            print("Numero de carta incorrecto")
        else:
            player.hand_cards.remove(card)
            table.giveCard(card)
            return True


# funcion take: El jugador toma cartas de la mesa utilizando una de sus cartas que tengan el mismo valor
# PARAMETROS:
# player; El jugador que va a tomar.
# table: mesa del juego.
# RETORNO
# True si el jugador toma las cartas.
# False si el jugador decide no tomar y hacer otro tipo de movida.
def take(player, table):
    card = None
    successful_take = False
    while card is None and successful_take is False:
        position_to_take = int(input("Cual posicion de la mesa desea tomar (si desea hacer otro tipo de jugada, escriba 0): "))
        if position_to_take == 0:
            return False
        card_to_take = input("Eliga la carta que utilizara para tomar (si desea hacer otro tipo de jugada, escriba 0): ")
        if card_to_take == '0':
            return False
        card = player.search_card(card_to_take)
        if card is None:
            print("Numero de carta incorrecto")
        elif card is not None and Table.sum_card_row_value(table.cards[position_to_take-1]) == card.value:
            for x in table.cards[position_to_take-1]:
                player.gained_cards.append(x)
            player.gained_cards.append(card)
            table.cards.pop(position_to_take-1)
            player.hand_cards.remove(card)
            successful_take = True
            print("Cartas tomadas con exito!")
            return successful_take, player
        else:
            print("No puede tomar de la mesa con esa carta!")


# funcion build: Construye cartas en la mesa con una carta en la mano del jugador.
# PARAMETROS:
# player: El jugador que realizara la construccion.
# table: mesa del juego.
# RETORNO:
# True si el jugador completa la construccion.
# False si el jugador decide no completar la construccion y hacer otro tipo de movida.
def build(player, table):
    card = None
    successful_build = False
    while card is None and successful_build is False:
        try:
            position = int(input("Sobre que posicion deseas construir (si desea hacer otro tipo de jugada, escriba 0): "))
            if position == 0:
                return False
            card_to_build = input("Escribe la carta que desea utilizar para construir (si desea hacer otro tipo de jugada, escriba 0): ")
            if card_to_build == '0':
                return False
            card = player.search_card(card_to_build)
            if card is None:
                print("Numero de carta incorrecto")
            else:
                if int(Table.sum_card_row_value(table.cards[position-1])) + int(card.value) <= 13:
                    table.build_card(card, position)
                    player.hand_cards.remove(card)
                    successful_build = True
                    extend_build = input("Va a extender la construccion? Si (1), No (Cualquier digito)")
                    if extend_build == "1":
                        extra_build(position, table)
                    return successful_build
                else:
                    print("No es posible construir en esa posicion!")
        except ValueError:
            print("No es posible construir en esa posicion!")


# funcion extra_build: Construye cartas que ya se encuentra en la mesa
# PARAMETROS:
# position: cartas que se usaran para construir con otra carta en la mesa
# table: mesa del juego
# RETORNO:
# No hay retorno.
def extra_build(position, table):
    successful_extra_build = False
    while successful_extra_build is False:
        try:
            new_position = int(
                input("En cual posicion construira? (si desea cancelar la construccione extra, escriba 0): "))
            if new_position == 0:
                return True
            if Table.sum_card_row_value(table.cards[new_position - 1]) == Table.sum_card_row_value(table.cards[position - 1]):
                for x in table.cards[position - 1]:
                    table.build_card(x, new_position)
                    table.cards.pop(position - 1)
                successful_extra_build = True
            else:
                print("No es posible construir en esa posicion!")
        except ValueError:
            print("No es posible construir en esa posicion!")



start()