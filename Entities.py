class Card:
    def __init__(self, number, sign, value):
        self.number = number
        self.sign = sign
        self.value = value


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