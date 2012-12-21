from __future__ import print_function

from players import is_empty
from header import header
from console_io import ConsoleCompleter, read_line

print('Please enter the names of the players in the game, one at a time.')
print('Please press <Enter> on a blank line when finished.')

# The players variable is a mapping from the player's name to the amount of
# games they have won.
# Same as players = dict() which creates a dictionary called 'players.'
players = {}

# Records names of people playing.
while True:
    name = read_line('Player {0}: '.format(len(players) + 1))
    if is_empty(name):
        break
    players[name] = 0    

compl = ConsoleCompleter(players.keys())

# Prints initial wins then prompts for the winner of each game.
while True:

    # Prints current wins for each player.
    print()
    print(header('Current Standings'))
    for name, wins in players.iteritems():
        print('{0}: {1}'.format(name, wins))
    print()

    # Adds one to the winner's score.
    winner = read_line('Please enter the name of the player that won: ')
    if is_empty(winner):
        break
    players[winner] += 1
    
