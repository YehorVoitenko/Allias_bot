from sqlalchemy import Integer
from sqlalchemy import Column
from sqlalchemy import String

from constants.tables import TEAM_TABLE
from repositories.base import Base as Base


class Team(Base):
    __tablename__ = TEAM_TABLE

    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    def __init__(self, name=None):
        self.name = name
