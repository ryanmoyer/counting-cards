#!/usr/bin/env python

import unittest

from header import header


class TestHeader(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(header(''), '\n')

    def test_default(self):
        self.assertEqual(
            header('This is a test'),
            'This is a test\n'
            '==============')

    def test_custom_char(self):
        self.assertEqual(
            header('Just a header', '#'),
            'Just a header\n'
            '#############')

    def test_just_spaces(self):
        self.assertEqual(
            header('       ', '%'),
            '       \n'
            '%%%%%%%')

    def test_tabs(self):
        # Python will treat the tab as just one character. Since we
        # don't know the size of tab stops, we will just treat it that
        # way as well. Solution: Don't use TABs in your header.
        self.assertEqual(
            header('Tab\tincoming', '*'),
            'Tab' '\t' 'incoming\n'
            '***' '*'  '********')
