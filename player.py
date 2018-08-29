from toolbox1 import get_integer_between

class Player(object):
    insurance = False
    insuranceBet = 0
    surrender = False
    def __init__(self, name, money):
        self.hands = []
        self.money = money
        self.name = name
        self.table = None

    def __str__(self):
        s = f'{self.name} ${self.money}'
        if self.hands:
            for hand in self.hands:
                s += f'\n{hand}'
        else:
            s += '\nNo hands'
        return s

    def sit(self, table):
        """Adds a player to the table"""
        self.table = table
        table.add_player(self)

    def bet_or_leave(self):
        """Finds if user wants to bet, pass, or leave."""
        play = 'x'
        validPlays = ['bet', 'b', 'pass', 'p', 'leave', 'l']
        while play not in validPlays:
            play = input(f"{self.name} (${self.money}), would you like to bet, pass, or leave? ")
        #
        # Finds the amount the player wants to bet inbetween 1 and their
        # amount of money.
        #
        if play == 'bet' or play == 'b':
            bet = get_integer_between('How much do you want to bet? ', 1, self.money, 0)
        #
        # Sets bet = to a value that the user would normally not be
        # able to enter. Where bet returns will use these numbers to
        # decide what to do with the player
        #
        elif play == 'leave' or play == 'l':
            bet = -1
        elif play == 'pass' or play == 'p':
            bet = 0
        return bet

    def rake_in(self, bet):
        """Adds money to the players money variable"""
        self.money += bet

    def add_hand(self, hand):
        """Adds a hand to the player"""
        self.hands.append(hand)

    def discard(self):
        """Gets rid of all hands for the player"""
        self.hands = []

    def play(self):
        """Gets the option the user wants to play"""
        #
        #
        #
        plays = {'s': '[S]tand',
                 'h': '[H]it',
                 'p': 'S[P]lit',
                 'd': '[D]ouble down',
                 'i': '[I]nsurance'}
        self.menu()
        validInputs = plays.key
        s()
        userInput = 'x'
        #
        # Gets the option the user wants to play and then returns it
        #
        while userInput not in validInputs:
            userInput = input('Command: ')[0].lower()
        return userInput

    def menu(self):
        """Prints the options for the player"""
        print("""
        Choices:
        [S]tand
        [H]it
        S[P]lit
        [D]ouble Down
        [I]nsurance
        """)

    def rake_out(self, bet):
        """Takes out money from the player"""
        self.money -= bet

    def insurance(self, sideBet):
        """Changes insurance to true and changes the insurance bet"""
        self.insurance = True
        self.insuranceBet = sideBet

    def is_insured(self):
        """Returns if the player is insured or not"""
        return self.insurance