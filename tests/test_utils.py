import unittest

from counting_cards.utils import is_empty


class TestUtils(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(is_empty(''))

    def test_string_with_spaces(self):
        self.assertTrue(is_empty('   '))

    def test_name(self):
        self.assertFalse(is_empty('Ryan'))
