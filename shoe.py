from deck import Deck
from card_obj import Card
from random import randint
import random
from toolbox1 import is_integer

class Shoe(list):

    debugMode = False

    def __init__(self, decks):
        super().__init__(self)
        self.decks = decks
        Shoe.populate_shoe(self)

    def __str__(self):
        string = 'Shoe: '
        for item in self:
            if Card.is_showing(item) == True:
                pass
            else:
                Card.flip(item)
            string = string + str(item) + ', '
        return string

    def add_plastic(self, decks):
        if decks == 1:
            number = randint(0, (decks - 1))
        else:
            number = randint(1, (decks - 1))
        deck = self[number]
        spot = randint(0, 51)
        plastic = 'plastic'
        deck.insert(spot, plastic)
        return self

    def cut_card(self):
        """Creates a cut card from at least 40 """
        minLength = 40
        self.cutCard = minLength + randint(0, (len(self) - 40))

    def should_shuffle(self):
        """
        Once the length of the shoe is less than the cut card number
        should shuffle returns true indicating that the shoe should
        be reshuffled
        """
        return len(self) < self.cutCard

    def draw(self):
        """Draws a card from the shoe and returns it"""
        card = self.pop(0)
        if Card.is_showing(card) == True:
            pass
        else:
            Card.flip(card)
        return card

    def populate_shoe(self):
        """Clears the shoe and then creates a new deck with a cut card"""
        self.clear()
        if is_integer(self.decks) == True:
            for _ in range(self.decks):
                for card in Deck():
                    self.append(card)
            Shoe.cut_card(self)
        else:
            print('Could not make deck. Please enter an acceptable integer')
        return self

    def shuffle_shoe(self):
        """Shuffles the shoe with the current amount of decks"""
        Shoe.populate_shoe(self)
        random.shuffle(self)
        return self


