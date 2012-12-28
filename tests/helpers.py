import sys
import unittest
from cStringIO import StringIO

# Comment on populating stdin and capturing stdout: This is DEFINITELY
# not the best way to do this. The best way would be through
# dependency injection, i.e.,
#
#     if __name__ == '__main__':
#         main(sys.stdin, sys.stdout)
#
# However, in the interest of simplicity and "teachability", we're
# just going to monkey-patch sys.stdin and sys.stdout.


def populate_stdin(buffer):
    sys.stdin = StringIO(buffer)


class CaptureStdoutTestCase(unittest.TestCase):
    def setUp(self):
        # Allow capturing of stdout.
        sys.stdout = StringIO()

    def assert_stdout_equal(self, contents):
        self.assertEqual(sys.stdout.getvalue(), contents)

    def tearDown(self):
        sys.stdout.close()
