# Clase Card: Contiene las 52 cartas utilizadas en juego de cartas
# ATRIBUTOS
# number: El numero de la carta.
# sign: El simbolo de la carta (♥, ♦, ♣, ♠).
# value: El valor de la carta (2-10 valor normal, A = 1, J = 11, Q = 12, K = 13).
class Card:
    def __init__(self, number, sign, value):
        self.number = number
        self.sign = sign
        self.value = value

# Clase Player: Los jugadores del juego.

# ATRIBUTOS
# identifier: id del jugador.
# hand_cards: Cartas que el jugador posee en mano.
# gained_cards: Cartas que el jugador ha tomado.
# score: Puntuaje del jugador al final del juego.

# METODOS
# giveCard: le añade una carta a la mano del jugador, toma como parametro un objeto carta.
# show_cards: forma de imprimir todas las cartas que tiene el jugador en mano.
# show_gained_cards: forma de imprimir todas als cartas que el jugador ha recolectado.
# search_card: busca si el jugador posee en mano una carta, toma como parametro el numero y signo de la carta concatenados (EJ: 10♦).
# count_spades: Cuenta todas las cartas con el signo de ♠ que el jugador ha recolectado.
# big_casino: Determina si el jugador tiene un 10 de diamantes con motivo de otorgarle 2 puntos.
# small_casino: Determina si el jugador tiene un 2 de pica con motivo de otorgarle un punto.
# count_aces: Le otorga al jugar un punto por cada as que el jugador haya recolectado.
# show_score: Imprime el puntuaje del jugador.
class Player:
    def __init__(self, identifier):
        self.identifier = identifier
        self.hand_cards = []
        self.gained_cards = []
        self.score = 0

    def giveCard(self, card):
        self.hand_cards.append(card)

    def show_cards(self):
        for x in self.hand_cards:
            print(str(x.number) + x.sign, end=" ")

    def show_gained_cards(self):
        for x in self.gained_cards:
            print(str(x.number) + x.sign, end=" ")

    def search_card(self, card_elements):
        for x in self.hand_cards:
            if (str(x.number)+x.sign) == card_elements:
                return x
        return None

    def count_spades(self):
        total = 0
        for card in self.gained_cards:
            if card.sign == '♠':
                total += 1
        return total

    def big_casino(self):
        for card in self.gained_cards:
            if card.number == 10 and card.sign == '♦':
                return 2
        return 0

    def small_casino(self):
        for card in self.gained_cards:
            if card.number == 2 and card.sign == '♠':
                return 1
        return 0

    def count_aces(self):
        points = 0
        for card in self.gained_cards:
            if card.number == 'A':
                points += 1
        return points

    def show_score(self):
        print("Player " + str(self.identifier) + " score: " + str(self.score))


# Clase Table: Donde se encuentran las cartas que se encuentran en la mesa

# ATRIBUTOS
# cards: Las cartas que se encuentran en mesa.

# METODOS
# giveCard: Añade una carta a la mesa
# build_card: "construye" una o varias cartas encima de otra carta, toma como parametro la carta que se añade (card_to_add)
#   y sobre cual carta (position) se construira.
# print_table: Despliega las cartas de la mesa en pantalla.
# sum_card_row_value: Metodo estatico que calcula el valor (value) que tiene una fila de cartas que sean pasadas.

class Table:
    def __init__(self):
        self.cards = []

    def giveCard(self, card):
        self.cards.append([card])

    def build_card(self, card_to_add, position):
        self.cards[position-1].append(card_to_add)

    def print_table(self):
        for x in self.cards:
            for card in x:
                print(str(card.number) + card.sign, end=" ")
            print("")

    @staticmethod
    def sum_card_row_value(cards):
        value = 0
        for card in cards:
            value += card.value
        return value