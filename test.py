#!/usr/bin/env python

# Test runner

from __future__ import print_function
import unittest
import subprocess


def main():
    """First runs flake8 syntax checker. Equivalent to this on the
    command line::

        flake8 .

    Then runs unit test discovery. Equivalent to this on the command line::

        python -m unittest discover tests

    No need to return anything since :func:`unittest.main()` directly calls
    :func:`sys.exit()`.
    """
    print('Syntax check')
    subprocess.check_call(['flake8', '.'])
    print('Syntax OK')
    print('Unit tests')
    unittest.main(argv=['', 'discover', 'tests'])

if __name__ == '__main__':
    main()
