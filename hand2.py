from card_obj import Card
from shoe import Shoe

class Hand(list):

    def __init__(self, bet):
        super().__init__()
        self.bet = bet
        self.isBlackJack = False
        self.isBusted = False
        self.isStanding = False
        self.isSplit = False
        self.isDoubled = False

    def __str__(self):
        string = super().__str__()
        string += f" ({self.soft_value()},{self.hard_value()})"
        string += f" bet: ${self.bet:.2f}"
        return string

    def hard_value(self):
        value = 0
        for card in self:
            value += Card.get_hard_value(card)
        return value

    def soft_value(self):
        value = 0
        for card in self:
            value += Card.get_soft_value(card)
        return value

    def value(self):
        value = self.soft_value()
        if value > 21:
            value = self.hard_value()
        return value

    def can_hit(self):
        canHit = True
        if self.isBlackJack or self.isDoubled or self.isBusted or self.isStanding:
            canHit = False
        return canHit

    def hit(self, card):
        if not self.can_hit():
            raise TypeError('Not able to hit this hand')
        self.append(card)
        self.check_if_blackjack()
        self.check_if_21()
        self.check_if_busted()

    def stand(self):
        self.isStanding = True

    def can_split(self):
        """Finds out if the hand can be split"""
        #
        # You can't split a hand if the hand is greater than 2 cards
        #
        if len(self) == 2:
            name1 = Card.get_name(self[0])
            name2 = Card.get_name(self[1])
            if name1 == name2:
                canSplit = True
            else:
                canSplit = False
        else:
            canSplit = False
        return canSplit

    def split(self):
        if not self.can_split():
            raise TypeError("Can't split this hand")
        self.isSplit = True
        card = self.pop()
        return card

    def can_double(self):
        #
        # If you can hit you can also double down
        #
        return self.can_hit()

    def double_down(self, card, additionalBet = None):
        if additionalBet == None:
            additionalBet = self.bet
        if not self.can_double():
            raise TypeError("Can't double down on this hand: " + str(self))
        if additionalBet > self.bet:
            raise ValueError('Double Down bet can not be more than original bet.')
        if additionalBet <= 0:
            raise ValueError('Double Down bet can not be less than or equal to zero.')
        self.bet += additionalBet
        self.hit(card)
        self.isDoubled = True
        self.isStanding = True

    def check_if_blackjack(self):
        if (self.value() == 21) and (len(self) == 2):
            self.isBlackJack = True
            self.isStanding = True
        return self.isBlackJack

    def check_if_busted(self):
        if self.value() > 21:
            self.isBusted = True
        return self.isBusted

    def check_if_21(self):
        if self.value() == 21:
            self.isStanding = True


