# Author: Thomas Fenaroli
# Date: 02/12/2021
# Purpose: Create a class Deck that represents a deck of playing cards

from card import Card
from random import *


# Creates class Deck that represents a deck of playing cards
class Deck:
    # initializes instance variable
    def __init__(self):
        self.card_list = []

    # adds standard playing cards to card_list instance variable
    def add_standard_cards(self):
        for number in range(1, 14):
            for suit in range(1, 5):
                self.card_list.append(Card(number, suit))

    # shuffles cards in card_list instance variable
    def shuffle(self):

        i = 0
        while i < 52:
            rand_index_1 = randint(0, 51)
            rand_index_2 = randint(0, 51)

            temp = self.card_list[rand_index_1]
            self.card_list[rand_index_1] = self.card_list[rand_index_2]
            self.card_list[rand_index_2] = temp

            i += 1

    # creates smaller deck containing last five elements of card_list instance variable
    def deal(self, n):
        hand = Deck()

        i = 0
        while i < n:
            hand.card_list.append(self.card_list.pop())
            i += 1

        return hand
