from player import Player
from hand2 import Hand
from shoe import Shoe
from toolbox1 import get_integer, get_integer_between

class Dealer(Player):

    def __init__(self, name, money):
        super().__init__(name, money)
        self.shoe = Shoe(8)
        self.playingPlayers = []

    def sit_dealer(self, table):
        """Places the dealer at the table and gives the dealer a table"""
        self.table = table
        table.add_dealer(self)

    def play(self, hand):
        """Dealers playing method"""
        #
        # The dealer has 2 options, he can hit
        # or he can stand. If the value of his hand
        # is less than 17 he must hit, otherwise he stands.
        #
        if hand.value() < 17:
            play = 'h'
        else:
            play = 's'
        return play

    def take_bets(self):
        """Gets bets from player"""
        self.playingPlayers = []
        self.leaving = []
        for player in self.table.players:
            betAmount = player.bet_or_leave()
            #
            # betAmount -1 means the player is leaving the table
            # betAmount 0 means the player is passing this hand
            # anything above 0 and less than the players money
            # means the user wants to play
            #
            if betAmount == -1:
                self.table.remove_player(player)
                print(f'{player.name} is leaving the table\n')
            elif betAmount == 0:
                print(f'{player.name} is sitting out this round\n')
            elif betAmount > 0 and betAmount <= player.money:
                self.playingPlayers.append(player)
                player.rake_out(betAmount)
                self.rake_in(betAmount)
                player.add_hand(Hand(betAmount))
                print(f'{player.name} has bet ${betAmount:.2f}\n')
            else:
                print(f'{player.name} cannot play this round\n')

    def deal(self):
        """Deals out cards to each player"""
        #
        # If the shoe needs to be shuffled, it shuffles
        #
        if Shoe.should_shuffle(self.shoe):
            Shoe.shuffle_shoe(self.shoe)
        cards = 2
        #
        # Creates the players initial hands
        #
        for player in self.playingPlayers:
            for item in range(cards):
                card = self.shoe.draw()
                player.hands[0].hit(card)
            #
            # Checks to see if the player has 21,
            # blackjack, or is busted. These functions
            # change the variables for the hand.
            #
            player.hands[0].check_if_blackjack()
            player.hands[0].check_if_21()
            player.hands[0].check_if_busted()
        #
        # Creates the dealers hand
        #
        bet = 0
        self.add_hand(Hand(bet))
        self.hands[0].hit(self.shoe.draw())
        self.hands[0].hit(self.shoe.draw())
        hand = self.hands[0]
        print(f'\nDealers hand: {hand[0]}, hidden card')

    def play_hands(self):
        """Plays the hands for each player"""
        for player in self.playingPlayers:
            print(f'\nCurrent player: {player.name}')
            for hand in player.hands:
                print(f'Hand: {hand}')
                while hand.can_hit():
                    #
                    # Gets the option for the user to play
                    #
                    userPlay = player.play()
                    if userPlay == 's':
                        hand.stand()
                    elif userPlay == 'h':
                        card = self.shoe.draw()
                        hand.hit(card)
                        print(hand)
                    elif userPlay == 'p':
                        if hand.can_split() and player.money >= hand.bet:
                            self.rake_in(hand.bet)
                            player.rake_out(hand.bet)
                            #
                            # Creates a new hand with the same bet.
                            #
                            newHand = Hand(hand.bet)
                            #
                            # Split returns the popped card from the
                            # original hand and hits it to the new hand.
                            #
                            newHand.hit(hand.split())
                            #
                            # Creates two more cards to make sure each hand
                            # has 2 cards.
                            #
                            card = self.shoe.draw()
                            newHand.hit(card)
                            player.add_hand(newHand)
                            card = self.shoe.draw()
                            hand.hit(card)
                            self.play_hands()
                        else:
                            print('You cannot split this hand, please choose another option')
                    elif userPlay == 'd':
                        if hand.can_double() and player.money >= hand.bet:
                            card = self.shoe.draw()
                            #
                            # Gets another bet from the user less than or
                            # equal to the original bet.
                            #
                            additionalBet = -1
                            while additionalBet < 0 or additionalBet > hand.bet:
                                additionalBet = get_integer('How much would you like to double down? ')
                            hand.double_down(card, additionalBet)
                            self.rake_in(additionalBet)
                            player.rake_out(additionalBet)
                            print(player)
                    elif userPlay == 'i':
                        if player.is_insured():
                            sideBet = hand.bet + 1
                            while sideBet > hand.bet:
                                sideBet = get_integer("How much do you want to bet for insurance? ")
                            player.insurance(sideBet)
                        else:
                            print("You are already insured")
                    else:
                        print(f"I'm sorry, I don't know what '{userPlay}' means.")
        #
        # A method for the dealer to make
        # sure his hand has a value greater
        # than 17
        #
        while self.hands[0].value() < 17:
            card = self.shoe.draw()
            self.hands[0].hit(card)
            print(f'Dealer draws: {card}')
        print(f'Dealers hand: {self.hands[0]}')