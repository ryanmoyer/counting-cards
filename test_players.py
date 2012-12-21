import unittest

from players import is_empty

class TestPlayers(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(is_empty(''))

    def test_string_with_spaces(self):
        self.assertTrue(is_empty('   '))

    def test_name(self):
        self.assertFalse(is_empty('Ryan'))

if __name__ == '__main__':
    unittest.main()
