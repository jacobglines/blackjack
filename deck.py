from card_obj import Card
import random


class Deck(list):

    def __init__(self):
        super().__init__(self)
        for suit in Card.suits:
            for item in Card.names:
                self.append(Card(item, suit))
        Deck.shuffle_deck(self)
        self.cardsInDeck = Deck.length(self)

    def __str__(self):
        string = f'{self.cardsInDeck} cards in this deck: '
        for item in self:
            Card.flip(item)
            string = string + str(item) + ', '
        return string

    def length(self):
        """"Finds the amount of cards in the deck"""
        cardsInDeck = len(self)
        return cardsInDeck

    def shuffle_deck(self):
        """Once cards have been put in the deck, this function shuffles it"""
        random.shuffle(self)
        return self
