from hand2 import Hand

class Table(object):
    def __init__(self):
        self.players = []
        self.dealer = None

    def add_player(self, player):
        """Adds a player to the table"""
        self.players.append(player)

    def add_dealer(self, dealer):
        """Adds a dealer to the table"""
        self.dealer = dealer

    def remove_player(self, player):
        """Removes a player from the table"""
        self.players.remove(player)

    def payout(self, dealer):
        """Pays each player"""
        for player in dealer.playingPlayers:
            for hand in player.hands:
                if hand.check_if_blackjack():
                    bet = hand.bet * 1.5
                    round(bet, 1)
                    #
                    # Player gets back their bet and blackjack
                    # pays out 3 to 2 (1.5x)
                    #
                    bet += hand.bet
                    player.rake_in(bet)
                    print(f'Nice! {player.name} got blackjack this hand. You earned ${bet:.2f}\n')
                elif dealer.hands[0].check_if_blackjack() and player.is_insured():
                    #
                    # Player gets their bet back and what they earned from itt
                    #
                    player.rake_in(player.insuranceBet * 2)
                    print(f'{player.name} won ${player.insuranceBet} by insurance ')
                elif Hand.check_if_busted(dealer.hands[0]) == True and hand.check_if_busted() == False:
                    print(f"Dealer busts, {player.name} earned ${hand.bet:.2f}\n")
                    player.rake_in(hand.bet * 2)
                else:
                    bet = hand.bet
                    if hand.value() <= 21 and hand.value() > dealer.hands[0].value():
                        player.rake_in(hand.bet * 2)
                        print(f'{player.name} won! You earned ${bet:.2f}\n')
                    elif hand.value() == dealer.hands[0].value():
                        player.rake_in(hand.bet)
                        print(f'{player.name} tied with the dealer, you got ${bet:.2f} back.\n')
                    else:
                        print(f'{player.name} lost.\n')

    def intro(self):
        """Prints introduction the the program"""
        print("""
======================================================================
=                                                                    =  
=                            Blackjack                               =
=                                                                    =
======================================================================""")

    def outro(self):
        """Prints outro to the program"""
        print("Thank you for playing!")

    def instructions(self):
        """Prints the instructions to the program"""
        print("""
        Instructions:
        This game is Blackjack the popular card game.
        When playing you will play until you run out
        of money or decide to leave.""")



