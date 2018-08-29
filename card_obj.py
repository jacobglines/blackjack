class Card(list):
    suits = ['clubs', 'spades', 'hearts', 'diamonds']
    unicode = ['\u2663', '\u2660', '\u2661', '\u2662']

    unicodeDict = dict(zip(suits, unicode))

    names = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
    shortNames = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    shortNameDict = dict(zip(names, shortNames))

    hardValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    softValues = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    hardValueDict = dict(zip(names, hardValues))
    softValueDict = dict(zip(names, softValues))

    ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11, 12, 13]
    rankDict = dict(zip(names, ranks))

    useUnicode = True

    debugMode = False

    def __init__(self, name, suit):
        super().__init__(self)
        #
        # Check that the name is a legal name.
        #
        if name.lower() in Card.names:
            self.__name = name.lower()
            self.__shortName = Card.shortNameDict[self.__name]
        #
        # Or that name is a legal short name, just in case.
        #
        elif name.upper() in Card.shortNames:
            name = Card.names[Card.shortNames.index(name.upper())]
            self.__name = name.lower()
            self.__shortName = Card.shortNameDict[self.__name]
        else:
            raise TypeError(name + ' is not a valid card name.')
        #
        # Check that the suit is legal
        #
        if suit.lower() in Card.suits:
            self.__suit = suit.lower()
        else:
            raise TypeError(suit + ' is not a valid card suit.')
        #
        # Check if it is a facecard
        #
        if self.__name in ['jack', 'queen', 'king']:
            self.__isFacecard = True
        else:
            self.__isFacecard = False
        #
        # Check if it is an ace
        #
        if self.__name == 'ace':
            self.__isAce = True
        else:
            self.__isAce = False
        self.__showing = False
        self.__rank = Card.rankDict[self.__name]
        self.__hardValue = Card.hardValueDict[self.__name]
        self.__softValue = Card.softValueDict[self.__name]

    def __str__(self):
        if Card.useUnicode:
            string = f'{self.__name} of {self.__suit}'
        else:
            string = f'{self.__name.capitalize()} of {self.__suit.capitalize()}'
        if not self.__showing and not Card.debugMode:
            string = '[face down]'
        return string

    def __repr__(self):
        return f"{self.name} of {self.suit}"

    def flip(self):
        """Flips the card over from 'showing' to 'not showing' or visa versa."""
        self.__showing = not self.__showing

    def is_showing(self):
        """Returns True if the card is face-up and can be seen."""
        return self.__showing

    def get_facecard(self):
        """Returns True if the card is a facecard."""
        if not self.is_showing():
            raise RuleError('card is not showing, you can not use is_face_card()')
        return self.__isFacecard

    def get_ace(self):
        """Returns True if the card is an ace."""
        if not self.is_showing():
            raise RuleError('card is not showing, you can not use is_ace()')
        return self.__isAce

    def get_hard_value(self):
        """Returns the hard value of the card."""
        if not self.is_showing():
            raise RuleError('card is not showing, you can not use hard_value()')
        return self.__hardValue

    def get_soft_value(self):
        """Returns the soft value of the card."""
        if not self.is_showing():
            raise RuleError('card is not showing, you can not use hard_value()')
        return self.__softValue

    def get_suit(self):
        """Returns the suit of the card."""
        if not self.is_showing():
            raise RuleError('card is not showing, you can not use suit()')
        return self.__suit

    def get_name(self):
        """Returns the name of the card."""
        if not self.is_showing():
            raise RuleError('card is not showing, you can not use name()')
        return self.__name

    def get_rank(self):
        """Returns the rank of the card."""
        if not self.is_showing():
            raise RuleError('card is not showing, you can not use rank()')
        return self.__rank

    facecard = property(get_facecard)
    ace = property(get_ace)
    hard_value = property(get_hard_value)
    soft_value = property(get_soft_value)
    suit = property(get_suit)
    name = property(get_name)
    rank = property(get_rank)

if __name__ == '__main__':

    import unittest

    class CardTester(unittest.TestCase):

        def test_is_showing(self):
            c = Card('ace', 'spades')
            #
            # Turn card face up (they start face down).
            #
            c.flip()
            self.assertTrue(c.is_showing())
            self.assertTrue(c.ace)
            self.assertFalse(c.facecard)
            self.assertEqual(c.rank, 1)
            self.assertEqual(c.name, 'ace')
            self.assertEqual(c.suit, 'spades')
            self.assertEqual(c.soft_value, 11)
            self.assertEqual(c.hard_value, 1)
            #
            # Turn card face down.
            #
            c.flip()
            self.assertFalse(c.is_showing())
            with self.assertRaises(RuleError):
                c.ace
                c.facecard
                c.rank
                c.name
                c.suit
                c.soft_value
                c.hard_value

        def test_equality(self):
            c1 = Card('ace', 'spades')
            c2 = Card('ace', 'hearts')
            c3 = Card('king', 'spades')
            c4 = Card('queen', 'spades')

            self.assertTrue(c1 == c2, 'Cards with the same name should be equal.')
            self.assertFalse(c1 == c3, 'Cards with the same suit are not necessarily equal.')
            self.assertFalse(c3 == c4, 'Cards with the same value are not necessarily equal.')

    unittest.main(verbosity=2)
