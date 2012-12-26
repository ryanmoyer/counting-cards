import unittest

from db import PlayersDB, DuplicatePlayerError, NonexistentPlayerError


class TestPlayersDB(unittest.TestCase):
    def setUp(self):
        self.db = PlayersDB()

    def test_add_normal(self):
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
        wins = 10
        self.db.add_player(name)
        self.db.add_wins(name, wins)
        self.assertEqual(self.db.get_wins(name), wins)

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
