from utils.db_utils.teams import FirstTeam, SecondTeam
from repositories.base import Session

session = Session()


def add_first_team_info(name: str):
    t = FirstTeam(name=name)
    session.add(t)
    session.commit()


def add_second_team_info(name: str):
    t = SecondTeam(name=name)
    session.add(t)
    session.commit()
