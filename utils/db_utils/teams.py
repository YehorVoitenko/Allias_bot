from sqlalchemy import Integer
from sqlalchemy import Column
from sqlalchemy import String

from constants.tables import FIRST_TEAM_TABLE, SECOND_TEAM_TABLE
from repositories.base import Base as Base


class FirstTeam(Base):
    __tablename__ = FIRST_TEAM_TABLE

    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    def __init__(self, name=None):
        self.name = name


class SecondTeam(Base):
    __tablename__ = SECOND_TEAM_TABLE

    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    def __init__(self, name=None):
        self.name = name
