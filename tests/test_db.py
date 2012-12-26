import unittest

from counting_cards.db import (PlayersDB,
                               DuplicatePlayerError,
                               NonexistentPlayerError)


class TestPlayersDB(unittest.TestCase):
    def setUp(self):
        self.db = PlayersDB()

    def test_add_retrieve(self):
        name = 'Charlie'
        self.db.add_player(name)
        self.assertEqual(self.db.get_wins(name), 0)

    def test_add_duplicate(self):
        name = 'Ryan'
        self.db.add_player(name)
        with self.assertRaises(DuplicatePlayerError) as cm:
            self.db.add_player(name)
        self.assertEqual(str(cm.exception), 'Player already exists: Ryan')

    def test_add_wins(self):
        name = 'Mott'
        self.db.add_player(name)
        self.db.add_wins(name, 5)
        self.db.add_wins(name, 3)
        self.assertEqual(self.db.get_wins(name), 8)

    def test_add_wins_nonexistent(self):
        name = 'Fake'
        wins = 11
        with self.assertRaises(NonexistentPlayerError) as cm:
            self.db.add_wins(name, wins)
        self.assertEqual(str(cm.exception), 'No such player: Fake')

    def test_add_default_wins_is_one(self):
        name = 'Rick'
        self.db.add_player(name)
        self.db.add_wins(name)
        self.assertEqual(self.db.get_wins(name), 1)

    def test_multiple_players(self):
        self.db.add_player('Rick')
        self.db.add_player('Mott')
        self.db.add_wins('Rick')
        self.db.add_wins('Mott')
        self.db.add_wins('Rick')
        self.db.add_wins('Rick', 2)
        self.db.add_wins('Mott')
        self.assertEqual(self.db.get_wins('Rick'), 4)
        self.assertEqual(self.db.get_wins('Mott'), 2)

    def test_iter_players_wins(self):
        players_scores = [
            ('Kathy', 10),
            ('Ryan', 12),
            ('Steve', 6)]
        for name, wins in players_scores:
            self.db.add_player(name)
            self.db.add_wins(name, wins)
        # The players should be returned in the order which they were
        # added.
        self.assertEqual(list(self.db.iter_players_wins()), players_scores)

    def test_len_no_players(self):
        self.assertEqual(len(self.db), 0)

    def test_len_with_players(self):
        for name in ['Bruce', 'Bob', 'Sue']:
            self.db.add_player(name)
        self.assertEqual(len(self.db), 3)
