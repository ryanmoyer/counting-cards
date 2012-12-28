from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists

engine = create_engine('sqlite:///:memory:')
Session = sessionmaker()
Base = declarative_base()


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    wins = Column(Integer)

    def __repr__(self):
        return 'Player(name={0}, wins={1})'.format(self.name, self.wins)

Base.metadata.create_all(engine)


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
    def __init__(self, session=Session(bind=engine)):
        # If the user passes is a session, use that. Otherwise default
        # to a session bound to the engine. This is mainly for unit
        # testing.
        self.session = session

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
        self.session.flush()

    def add_wins(self, name, wins=1):
        winning_player = self._get_player_by_name(name)
        winning_player.wins += wins
        self.session.flush()

    def get_wins(self, name):
        player = self._get_player_by_name(name)
        return player.wins

    def get_players(self):
        return [row.name for row in self.session.query(Player.name).all()]

    def iter_players_wins(self):
        return iter([
            (row.name, row.wins) for row in self.session.query(
                Player.name, Player.wins).all()])
