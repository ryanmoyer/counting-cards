import unittest

from counting_cards.console_io import ConsoleCompleter, read_line
from tests.helpers import populate_stdin, CaptureStdoutTestCase


class TestConsoleCompleter(unittest.TestCase):
    def test_no_completions(self):
        cc = ConsoleCompleter([])
        self.assertIsNone(cc._readline_completer('hello', 0))

    def test_default_is_no_completions(self):
        cc = ConsoleCompleter([])
        self.assertIsNone(cc._readline_completer('hello', 0))

    def test_no_matches(self):
        cc = ConsoleCompleter(['Ryan', 'Sean', 'Kathy'])
        self.assertIsNone(cc._readline_completer('H', 0))

    def test_simple_completion(self):
        cc = ConsoleCompleter(['Ryan', 'Sean', 'Kathy'])
        self.assertEqual(cc._readline_completer('R', 0), 'Ryan')
        self.assertIsNone(cc._readline_completer('R', 1))

    def test_multiple_completion(self):
        cc = ConsoleCompleter(['Ryan', 'Sean', 'Rick', 'Kathy', 'Ron'])
        self.assertEqual(cc._readline_completer('R', 0), 'Ryan')
        self.assertEqual(cc._readline_completer('R', 1), 'Rick')
        self.assertEqual(cc._readline_completer('R', 2), 'Ron')
        self.assertIsNone(cc._readline_completer('R', 3))

    def test_case_insensitive(self):
        cc = ConsoleCompleter(['Jeff', 'Sean', 'jArED', 'Kathy', 'john'])
        self.assertEqual(cc._readline_completer('J', 0), 'Jeff')
        self.assertEqual(cc._readline_completer('J', 1), 'jArED')
        self.assertEqual(cc._readline_completer('J', 2), 'john')
        self.assertIsNone(cc._readline_completer('J', 3))

    def test_duplicate_case_insensitive(self):
        cc = ConsoleCompleter(['Martha', 'martha', 'mARTHA'])
        self.assertEqual(cc._readline_completer('m', 0), 'Martha')
        self.assertEqual(cc._readline_completer('m', 1), 'martha')
        self.assertEqual(cc._readline_completer('m', 2), 'mARTHA')
        self.assertIsNone(cc._readline_completer('m', 3))


class TestReadLine(CaptureStdoutTestCase):
    def test_normal_usage(self):
        populate_stdin('awesome\n')
        self.assertEqual(read_line('fake prompt'), 'awesome')
        self.assert_stdout_equal('fake prompt')

    def test_empty_line(self):
        populate_stdin('\n')
        self.assertEqual(read_line('fake prompt'), '')
        self.assert_stdout_equal('fake prompt')

    def test_eof(self):
        # Populate stdin with an empty string. This will cause an
        # EOF. In the interest of simplicity, just return this as an
        # empty string. These are the same:
        #
        #     sys.stdin = StringIO()
        #     sys.stdin = StringIO('')
        #
        populate_stdin('')
        self.assertEqual(read_line('my prompt'), '')
        self.assert_stdout_equal('my prompt')
