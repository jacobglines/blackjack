from table import Table
from dealer import Dealer
from toolbox1 import get_integer_between, get_integer, get_yes_no
from player import Player

def main():
    table = Table()
    table.intro()
    userInput = get_yes_no("\nWould you like to see the instructions? ")
    if userInput == 'yes':
        table.instructions()
    dealer = Dealer('jacob', 999999999)
    numberOfPlayers = get_integer("\nHow many players are playing? ")
    for numb in range(numberOfPlayers):
        name = input('Please enter a name: ')
        money = get_integer_between(f"How much money does {name} have? ", 1, 100000, 0)
        player = Player(name, money)
        player.sit(table)
        print('\n')
    Dealer.sit_dealer(dealer, table)
    dealer.take_bets()
    while len(table.players) > 0:
        dealer.deal()
        dealer.play_hands()
        table.payout(dealer)
        for player in table.players:
            player.discard()
        dealer.discard()
        dealer.take_bets()
    table.outro()

main()
