# Author: Thomas Fenaroli
# Date: 02/12/2021
# Purpose: Create a class Card that represents a playing card and has two class attributes: value and suit

# Creates class Card that represents a playing card and has two class attributes: value and suit
class Card:
    # initializes instance variables
    def __init__(self, value, suit):
        if value == 11:
            self.value = "Jack"
        elif value == 12:
            self.value = "Queen"
        elif value == 13:
            self.value = "King"
        elif value == 1:
            self.value = "Ace"
        else:
            self.value = value

        if suit == 1:
            self.suit = "clubs"
        elif suit == 2:
            self.suit = "spades"
        elif suit == 3:
            self.suit = "diamonds"
        else:
            self.suit = "hearts"

    # returns card as string
    def __str__(self):
        return str(self.value) + " of " + str(self.suit)