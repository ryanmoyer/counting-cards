"""
:mod:`header`
~~~~~~~~~~~~~

Output a pretty header like this::

  This Is My Header Text
  ======================

:copyright: (C) 2012 Sean Fisk
:license: Public Domain

"""


def header(header_text, char='='):
    """Print text from a header and a line of header characters below it.

    :param header_text: the text to print
    :type header_text: :class:`str`
    :param char: (optional) the character with which to form the line
    :type char: :class:`str`

    :returns: the full header with line in a string
    :rtype: :class:`str`
    """
    return header_text + '\n' + len(header_text) * char
