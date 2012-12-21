"""This module allows easy use of readline completion function and
easy input.

First, import the necessary names::

    >>> from console_io import ConsoleCompleter, read_line

To use completion, first set up a ``ConsoleCompleter`` with a list of
completions::

    >>> compl = ConsoleCompleter(['milk', 'eggs', 'cheese', 'chicken'])

Now use ``read_line()`` to read input::

    >>> item = read_line('Enter an item: ')

On the console, completion will occur on the typed text when <Tab> is
pressed::

    Enter an item: m<Tab>
    Enter an item: milk

Text with multiple completions will show below the prompt when <Tab>
is pressed twice::

    Enter an item: c<Tab><Tab>
    cheese chicken
    Enter an item: ch<Tab>
    Enter an item: chicken
"""

from __future__ import print_function
# Uses GNU readline on UNIX-like operating systems, pyreadline on Windows.
import readline

# Set up global readline state.
readline.parse_and_bind('tab: complete')    
    
class ConsoleCompleter(object):
    """Track completions for a readline completer function."""
    def __init__(self, completions=[]):
        self.completions = completions
        # Tell readline to use the tab key for completions.
        readline.set_completer(self._readline_completer)
            
    def _readline_completer(self, text, state):
        # This is a clever way to return the correction completion for
        # the "state". Basically, the "state" is the amount of times
        # tab has been pressed. This code decrements state to find the
        # nth completion starting with the text.
        for completion in self.completions:
            if completion.lower().startswith(text.lower()):
                if state == 0:
                    return completion
                else:
                    state -= 1

def read_line(prompt):
    """Easily accept input. When <Ctrl-D> (UNIX-like) or <Ctrl-Z> +
    <Enter> (Windows) is pressed to send the EOF character, just
    return an empty string instead."""
    try:
        return raw_input(prompt)
    except EOFError:
        # Simplify catching this to just returning an empty string.
        return ''
