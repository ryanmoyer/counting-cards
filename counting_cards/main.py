from __future__ import print_function

from counting_cards.utils import is_empty
from counting_cards.header import header
from counting_cards.console_io import ConsoleCompleter, read_line
from counting_cards.db import PlayersDB

print('Please enter the names of the players in the game, one at a time.')
print('Please press <Enter> on a blank line when finished.')

players = PlayersDB()

# Records names of people playing.
while True:
    name = read_line('Player {0}: '.format(len(players) + 1))
    if is_empty(name):
        break
    players.add_player(name)

compl = ConsoleCompleter(players.get_players())

# Prints initial wins then prompts for the winner of each game.
while True:

    # Prints current wins for each player.
    print()
    print(header('Current Standings'))
    for name, wins in players.iter_players_wins():
        print('{0}: {1}'.format(name, wins))
    print()

    # Adds one to the winner's score.
    winner = read_line('Please enter the name of the player that won: ')
    if is_empty(winner):
        break
    players.add_wins(winner)
