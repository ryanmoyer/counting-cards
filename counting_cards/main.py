from __future__ import print_function

from counting_cards.utils import is_empty
from counting_cards.header import header
from counting_cards.console_io import ConsoleCompleter, read_line
from counting_cards.db import PlayersDB


def print_current_standings(players_db):
    print()
    print(header('Current Standings'))
    for name, wins in players_db.iter_players_wins():
        print('{0}: {1}'.format(name, wins))
    print()


def main():
    players = PlayersDB()

    print_current_standings(players)

    print('Please enter the names of the players in the game, one at a time.')
    print('Please press <Enter> on a blank line when finished.')

    # Records names of people playing.
    while True:
        name = read_line('Player {0}: '.format(len(players) + 1))
        if is_empty(name):
            break
        players.add_player(name)

    ConsoleCompleter(players.get_players())

    # Prints initial wins then prompts for the winner of each game.
    while True:

        # Prints current wins for each player.
        print_current_standings(players)

        # Adds one to the winner's score.
        winner = read_line('Please enter the name of the player that won: ')
        if is_empty(winner):
            break
        players.add_wins(winner)

if __name__ == '__main__':
    main()
