from collections import OrderedDict


class DuplicatePlayerError(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Player already exists: {0}'.format(self.name)


class NonexistentPlayerError(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'No such player: {0}'.format(self.name)


class PlayersDB(object):
    def __init__(self):
        self._data = OrderedDict()

    def __len__(self):
        return len(self._data)

    def add_player(self, name):
        if name in self._data:
            raise DuplicatePlayerError(name)
        self._data[name] = 0

    def add_wins(self, name, wins=1):
        try:
            self._data[name] += wins
        except KeyError:
            raise NonexistentPlayerError(name)

    def get_wins(self, name):
        return self._data[name]

    def get_players(self):
        return self._data.keys()

    def iter_players_wins(self):
        return self._data.iteritems()
