import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from appdirs import user_data_dir

APP_NAME = 'Counting Cards'
APP_AUTHOR = 'Ryan Moyer'
SQLITE_DB_DIR = user_data_dir(APP_NAME, APP_AUTHOR)
if not os.path.exists(SQLITE_DB_DIR):
    os.makedirs(SQLITE_DB_DIR)  # No error handling for this (yet).
SQLITE_DB_PATH = os.path.join(SQLITE_DB_DIR, 'players.sqlite')

Session = sessionmaker()
Base = declarative_base()


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    wins = Column(Integer)

    def __repr__(self):
        return 'Player(name={0}, wins={1})'.format(self.name, self.wins)


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
    def __init__(self,
                 engine=create_engine('sqlite:///{0}'.format(SQLITE_DB_PATH)),
                 session=None):
        # If the user passes an engine and a session use them. This
        # "feature" will only be used for unit testing. The defaults
        # will be used for production.
        self.engine = engine
        if session is None:
            self.session = Session(bind=engine)
        else:
            self.session = session
        Base.metadata.create_all(engine)

    def __len__(self):
        return self.session.query(Player).count()

    def _get_player_by_name(self, name):
        player = self.session.query(Player).filter(Player.name == name).first()
        if player is None:
            # No rows were returned.
            raise NonexistentPlayerError(name)
        return player

    def add_player(self, name):
        if self.session.query(exists().where(Player.name == name)).scalar():
            raise DuplicatePlayerError(name)
        new_player = Player(name=name, wins=0)
        self.session.add(new_player)
        self.session.commit()

    def add_wins(self, name, wins=1):
        winning_player = self._get_player_by_name(name)
        winning_player.wins += wins
        self.session.commit()

    def get_wins(self, name):
        player = self._get_player_by_name(name)
        return player.wins

    def get_players(self):
        return [row.name for row in self.session.query(Player.name).all()]

    def iter_players_wins(self):
        return iter([
            (row.name, row.wins) for row in self.session.query(
                Player.name, Player.wins).all()])
